import re
import pandas as pd
import string
from collections import Counter
import nlp_basics as nlp
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF term frequency - inverted document frequency
# takes into account how many times a term appear and in how many docs
# if a term is not frequent (appears only once per doc) but it's present in all docs, its weigth is high
# if a term appears frequently in a few texts but not in many others, its weigth is lowered down

def text2Vector(texts):
	print("Vectorizing ...")
	tfidf_vectorizer = TfidfVectorizer(tokenizer=nlp.stemTokenizer, stop_words='english')
	vectors = tfidf_vectorizer.fit_transform(texts)
	return (vectors)

def cosine_similarity(vector):
    return (vector * vector.T).toarray()

def similarity_matrix(texts):
	vectors = text2Vector(texts)
	scores = cosine_similarity(vectors)
	return (scores)
