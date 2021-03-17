import pandas as pd
import nlp_basics as nlp
import topic_modelling as model  # term frequency vectorizer
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('complete.csv', delimiter=',', usecols=[1,2,3,4,5,6,7,8])
df.drop_duplicates(inplace=True)
# drop unrelated subjects
df = model.check_df(df)
# change title+abstract into a unique column of text
dataset = df.filter(['title','abstract'], axis=1)
dataset['text'] = df['title'].str.cat(df[['abstract']].astype(str), sep=" ")
# remove stopwords and Nan values
# remove academic-reated words
dataset = nlp.normalize(dataset)
dataset = nlp.remove_academic_words(dataset)
# change dataset['text'] into a simple list
texts = dataset['text'].tolist()
# change texts into vectors of topics
tmodel, scores = model.topic_matrix(texts)
# add a new column with the found topic for each subject
df['topics'] = scores.argmax(axis=1)
# filter topics according to relevant keywords
keywords = ['adolescent','children','gifted']
topics = model.filter_topics(tmodel, keywords)
# filter df by relevant topics
mask = df['topics'].isin(topics)
df = df[mask]
# save df to csv and excel
df.to_csv('df.csv',index=False)
df.drop('topics', axis=1) # we don't need to give the topics to the client in excel
df.to_excel('results.xlsx')
# add test and train
# drop topics not fitted

#pd.set_option('display.max_colwidth', None)
# print(topics)
print(df)
