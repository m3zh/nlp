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

import nlp_basics as nlp
import spacy
from sense2vec import Sense2VecComponent
from tika import parser
import senseToVec as s2v

## script to create corpus from pdfs
# corpus = ""
# for i in range(3):
#     corpus += s2v.pdf_to_txt(i)
# corpus = nlp.remove_punctuation(corpus)
# with open('../pdfs/corpus.txt','w') as f:
#     f.write(corpus)

with open('../pdfs/corpus.txt','r') as f:
    corpus = f.read()
corpus = list(corpus.replace(r'\n',' ').replace(r'[\d+\\]','').split())


