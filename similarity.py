import nltk
import sklearn as sk
import clean_utilities as clean
import pandas as pd
import gensim

df = pd.read_csv('data.csv', delimiter=',', usecols=[1,2,3,4,5,6,7,8])
dataset = df.filter(['title','abstract'], axis=1)

dataset = clean.stop_words(dataset)
print(dataset)
