import re
import pandas as pd
import string
from collections import Counter
import nlp_basics as nlp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from flashtext import KeywordProcessor
import pickle
import numpy as np
from nltk.corpus import wordnet as wn
from pathlib import Path
from dict as d

# TF-IDF term frequency - inverted document frequency
# takes into account how many times a term appear and in how many docs
# if a term is not frequent (appears only once per doc) but it's present in all docs, its weigth is high
# if a term appears frequently in a few texts but not in many others, its weigth is lowered down

def reweighting(texts, keyword):
    with Path(__file__).parent.joinpath('syn.dict').open("rb") as f:
        syn_dict = dict(pickle.load(f))
    if keyword not in syn_dict:
        print("--------------------------------------------")
        print("Getting s2v synonyms ...")
        s2v_syns = d.s2v_synonyms(keyword)
        print("Synonyms collected:")
        print(' '.join(s2v_vec))
        user_syns = input("Wanna add other synonyms? Add them in a comma-separated list, e.g. my,wonderful synonyms,list\n").split(',')
        syn_dict[keyword] = set(s2v_syns.append(user_syns))
    else:
        print("--------------------------------")
        print("For this word, the following synonyms are already in dictionary: \n"+str(syn_dict[keyword]))
    synonym = { keyword : syn_dict[keyword] }
    processor = KeywordProcessor()
    processor.add_keywords_from_dict(synonym)
    texts = [processor.replace_keywords(t) for t in texts]
    with Path(__file__).parent.joinpath('syn.dict').open("wb") as f:
        pickle.dump(syn_dict, f)
    print("----------- dictionary updated -------------")
    return (texts)


# take a list of texts,
# change them into vectors
# and return a lists of vectors
def text2Vector(texts, keyword):
    print("Vectorizing ...")
    # in tokenizer, you can use either stemTokenizer or lemmaTokenizer
    tfidf_vectorizer = TfidfVectorizer(tokenizer=nlp.stemTokenizer)
    # attach more importance to search keywords
    texts = reweighting(texts, keyword)
    vectors = tfidf_vectorizer.fit_transform(texts)
    return (vectors)

# compute how close each vector is from the others
def cosine_similarity(vector):
    print("Computing similarity scores ...")
    return (vector * vector.T).toarray()

# returns a list of scores
# based on the similarity of each text
def similarity_matrix(texts, keyword):
    vectors = text2Vector(texts, keyword)
    scores = cosine_similarity(vectors)
    return (scores)

# normalize scores in a range from 0 to 1
def get_scores(rows, values):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scores = [np.sum(v) for v in values]
    scores = np.array(scores).reshape(rows, -1) # to fit the df shape
    return scaler.fit_transform(scores) # normalize 0, 1
