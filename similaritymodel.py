import tf_idf  # term frequency vectorizer
import numpy as np
import pandas as pd
import nlp_basics as nlp
import ds_basics as ds

def get_model(df, texts):
    # texts are feed to the model and turned into vectors of words
    vectors = tf_idf.similarity_matrix(texts)
    # compute similarity scores between text vectors
    # return a score between 0 and 1
    # add scores column to original df
    scores = tf_idf.get_scores(len(df),vectors)
    df['score'] = scores
    # set a minimum value of similarity
    # and discard texts that got a score lower than the minimum value
    df = ds.sort_df(df)
    # save the data in csv and xlsl
    df = df.drop('score',axis=1)
    df.to_csv("similarity_results.csv")
    df.to_excel("similarity_results.xlsx")
    print(df.shape)
    return (df)

# to display full-width column in df in terminal
# pd.set_option('display.max_colwidth', None)
# print(df)
