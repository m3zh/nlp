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
import spacy
from sense2vec import Sense2VecComponent
from tika import parser

def pdf_to_txt(pdf):
    with open('../pdfs/'+str(pdf)+'.pdf','rb') as pdf:
        raw = str(parser.from_file(pdf))
        text = raw.encode('utf-8', errors='ignore')
    return(raw.lower())