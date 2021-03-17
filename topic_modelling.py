import re
import pandas as pd
import string
from collections import Counter
import nlp_basics as nlp
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import NMF
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pickle

# transform texts into vectors
# dump the vectorizer in the file vectorizer.pickle
def text2Vector(texts):
    print("Vectorizing ...")
    # in tokenizer, you can use either stemTokenizer or lemmaTokenizer
    vectorizer = CountVectorizer(tokenizer=nlp.lemmaTokenizer, max_df=0.9, min_df=25, token_pattern='\w+|\$[\d\.]+|\S+')
    #vectorizer = CountVectorizer() # , stop_words='english') <- we can omit this parameter, as we remove stopwords upfront
    vectors = vectorizer.fit_transform(texts).toarray()
    pickle.dump(vectorizer, open("vectorizer.pickle", "wb"))
    return (vectors)

# NMF is better for shorter texts (such as tweets, titles) but less precise
# model used to extract topics
def NMF_model(vectors):
    print("NMF modelling ...")
    topics = 10
    tmodel = NMF(n_components=topics, random_state=42)
    scores = tmodel.fit_transform(vectors)
    return tmodel, scores

# LDA is better for long text and more precise in general
# model used to extract topics
def LDA_model(vectors):
    print("LDA modelling ...")
    topics = 10
    tmodel = LDA(n_components=topics, random_state=42)
    scores = tmodel.fit_transform(vectors)
    return tmodel, scores

# extract topic and assign one to each article
def topic_matrix(texts):
    vectors = text2Vector(texts)
    # LDA or NMF model
    tmodel, scores = LDA_model(vectors)
    return (tmodel, scores)

# keeps only topic with relevant keywords
def filter_topics(tmodel, keywords):
    keywords = nlp.get_lemmas(nlp.get_synonyms(keywords))
    vectorizer = pickle.load(open("vectorizer.pickle", 'rb'))
    topics = []
    for i, topic in enumerate(tmodel.components_):
        words = [vectorizer.get_feature_names()[i] for i in topic.argsort()[-5:]]
        # print(i)
        # print(words)
        for word in keywords:
            if re.search(word, ' '.join(words)):
                topics.append(i)
    return set(topics)

def check_df(df):
    keywords = ['engineering','cultural','forensic','natural']
    df = df[~df['subject'].astype(str).str.contains('|'.join(keywords),case=False)]
    return df
