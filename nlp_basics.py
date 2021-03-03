import re, nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.stem.porter import *
from collections import Counter

def remove_punctuation(original):
	# remove punctuation and numbers
	new = re.sub('['+string.punctuation+'|\d+?]', '', original)
	return (new)

def remove_stopwords(original):
	print("Removing stopwords ...")
	# you need to download the corpus on your machine -> python3 -m nltk.downloader stopwords
	# add nan to remove NaN
	sw_list = set(stopwords.words('english'))
	sw_list.add('nan')
	# add academic-specific words, e.g. analysis
	sw_list.update(['analysis','study','review','investigate','paper','research','model'])
	# use applymap for df, apply for Series
	new = original.applymap(lambda col: remove_punctuation(str(col).lower()))
	# remove stopwords
	new = new.applymap(lambda col: ' '.join([w for w in col.split() if w not in sw_list]))
	return (new)

# stem take only one token for words with different forms,
# e.g. give, gave, given -> stem: give
# note to self : lemmatisation when we'll have more abstracts?

def get_stems(texts): # in terminal python3 -m nltk.downloader punkt
	stemmer = nltk.stem.porter.PorterStemmer()
	return [stemmer.stem(token) for token in texts]

def stemTokenizer(text):
    return get_stems(nltk.word_tokenize(text.lower()))

def get_lemmas(tokens): # in terminal python3 -m nltk.downloader wordnet
    lemmer = nltk.stem.WordNetLemmatizer()
    return [lemmer.lemmatize(token) for token in tokens]

def lemmaTokenizer(text):
    return get_lemmas(nltk.word_tokenize(text.lower()))
