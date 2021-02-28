import pandas as pd
import nlp_basics as nlp
import topic_modelling as model  # term frequency vectorizer
import numpy as np

df = pd.read_csv('data.csv', delimiter=',', usecols=[1,2,3,4,5,6,7,8])
df.drop_duplicates(inplace=True)
# change title+abstract into a unique column of text
dataset = df.filter(['title','abstract'], axis=1)
dataset['text'] = df['title'].str.cat(df[['abstract']].astype(str), sep=" ")
# remove stopwords and Nan values
dataset = nlp.remove_stopwords(dataset)
# change dataset['text'] into a simple list
texts = dataset['text'].tolist()
# change texts into vectors of topics
scores = model.topic_matrix(texts)
# add a new column with the found topic for each subject
df['topics'] = scores.argmax(axis=1)
# get first two topics
#scores = model.filter_topics(len(df),vectors)
# add scores column to original df and sort

#df = df.sort_values(by=['topics'], ascending=False)

# add test and train
# drop topics not fitted

#pd.set_option('display.max_colwidth', None)
print(df)
