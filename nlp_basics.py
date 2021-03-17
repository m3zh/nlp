import re, nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.porter import *
from flashtext import KeywordProcessor
from collections import Counter
import pickle

# british to american english
def Be2AmE():
    eng = pickle.load(open("engdict.pickle","rb"))
    # eng = ast.literal_eval(data)
    processor = KeywordProcessor(eng)
    processor.add_keywords_from_dict(eng)
    return (processor)

def remove_punctuation(original):
    # remove punctuation and numbers
    new = re.sub('['+string.punctuation+'|\d+?]', '', original)
    return (new)

def normalize(original):
    print("Removing stopwords...")
    # need to download the corpus on your machine -> python3 -m nltk.downloader stopwords
    # add nan to remove NaN
    sw_list = set(stopwords.words('english'))
    sw_list.add('nan')
    # use applymap for df, apply for Series
    # remove punctuation and stopwords
    new = original.applymap(lambda col: remove_punctuation(str(col).lower()))
    new = new.applymap(lambda col: ' '.join([w for w in col.split() if w not in sw_list]))
    # standardize AmE and BE
    dict = Be2AmE()
    new = new.applymap(lambda col: dict.replace_keywords(str(col).lower()))
    return (new)

def remove_academic_words(original):
	print("Removing academic words ...")
	aw_words = ['analysis','study','review','investigate','investigation','paper','research','model','experiment','experimental','mechanism','application' \
				'method', 'role', 'behavior', 'behaviour', 'mechanism']
	aw_list = []
	# add academic-specific words, e.g. analysis
	for w in aw_words:
		for syn in wordnet.synsets(w):
			for l in syn.lemmas():
				aw_list.append(l.name())
	aw_list = set(aw_list)
	print(aw_list)
	# use applymap for df, apply for Series
	new = original.applymap(lambda col: ' '.join([w for w in col.split() if w not in aw_list]))
	return (new)

def get_synonyms(words):
	syn_list = []
	for w in words:
		for syn in wordnet.synsets(w):
			for l in syn.lemmas():
				syn_list.append(l.name())
	return (set(syn_list))

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
