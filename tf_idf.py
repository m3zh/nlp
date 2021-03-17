import re
import pandas as pd
import string
from collections import Counter
import nlp_basics as nlp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# TF-IDF term frequency - inverted document frequency
# takes into account how many times a term appear and in how many docs
# if a term is not frequent (appears only once per doc) but it's present in all docs, its weigth is high
# if a term appears frequently in a few texts but not in many others, its weigth is lowered down

# take a list of texts,
# change them into vectors
# and return a lists of vectors
def text2Vector(texts):
	print("Vectorizing ...")
	# in tokenizer, you can use either stemTokenizer or lemmaTokenizer
	tfidf_vectorizer = TfidfVectorizer(tokenizer=nlp.stemTokenizer) # , stop_words='english') <- we can omit this parameter, as we remove stopwords upfront
	vectors = tfidf_vectorizer.fit_transform(texts)
	return (vectors)

# compute how close each vector is from the others
def cosine_similarity(vector):
    print("Computing similarity scores ...")
    return (vector * vector.T).toarray()

# returns a list of scores
# based on the similarity of each text
def similarity_matrix(texts):
	vectors = text2Vector(texts)
	scores = cosine_similarity(vectors)
	return (scores)

# normalize scores in a range from 0 to 1
def get_scores(rows, values):
	scaler = MinMaxScaler(feature_range=(0, 1))
	scores = [np.sum(v) for v in values]
	scores = np.array(scores).reshape(rows, -1) # to fit the df shape
	return scaler.fit_transform(scores) # normalize 0, 1
