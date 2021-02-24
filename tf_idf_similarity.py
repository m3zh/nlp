import pandas as pd
import nlp_basics as nlp
import tf_idf  #term frequency vectorizer
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
vectors = tf_idf.similarity_matrix(texts)
scores = tf_idf.get_scores(len(df),vectors)
df['tfidf_score'] = scores
df = df.sort_values(by=['tfidf_score'], ascending=False)

#pd.set_option('display.max_colwidth', None)
print(df)
