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

# LDA is better for long text and more precise in general
# NMF is better for shorter texts (such as tweets, titles) but less precise

def text2Vector(texts):
	print("Vectorizing ...")
	# in tokenizer, you can use either stemTokenizer or lemmaTokenizer
	vectorizer = CountVectorizer(tokenizer=nlp.stemTokenizer, max_df=0.9, min_df=25, token_pattern='\w+|\$[\d\.]+|\S+')
	#vectorizer = CountVectorizer() # , stop_words='english') <- we can omit this parameter, as we remove stopwords upfront
	vectors = vectorizer.fit_transform(texts).toarray()
	#tf_feature_names = vectorizer.get_feature_names()
	return (vectors)

def NMF_model(vectors):
    print("NMF modelling ...")
    topics = 10
    model = NMF(n_components=topics, random_state=42)
    scores = model.fit_transform(vectors)
    return scores

def LDA_model(vectors):
    print("LDA modelling ...")
    topics = 10
    model = LDA(n_components=topics, random_state=42)
    scores = model.fit_transform(vectors)
    return scores

def topic_matrix(texts):
	vectors = text2Vector(texts)
	# LDA or NMP model
	scores = LDA_model(vectors)
	return (scores)
