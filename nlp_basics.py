import re, nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.stem.porter import *
from flashtext import KeywordProcessor
import pickle
import ast

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
    # you need to download the corpus on your machine -> python3 -m nltk.downloader stopwords
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

# stem take only one token for words with different forms,
# e.g. give, gave, given -> stem: give
def get_stems(texts): # in terminal python3 -m nltk.downloader punkt
    stemmer = nltk.stem.porter.PorterStemmer()
    return [stemmer.stem(token) for token in texts]

def stemTokenizer(text):
    return get_stems(nltk.word_tokenize(text.lower()))

# lemma take only one token for words with different forms,
# e.g. give, gave, given -> lemma: give
def get_lemmas(tokens): # in terminal python3 -m nltk.downloader wordnet
    lemmer = nltk.stem.WordNetLemmatizer()
    return [lemmer.lemmatize(token) for token in tokens]

def lemmaTokenizer(text):
    return get_lemmas(nltk.word_tokenize(text.lower()))
