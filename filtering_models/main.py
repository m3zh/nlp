import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import tf_idf  # term frequency vectorizer
import numpy as np
import pandas as pd
import nlp_basics as nlp
import pickle
from pathlib import Path

# sort scores, remove scores belowe a min value
# check results and return the final df, sorting by ascending sorting score
def sort_df(df, keywords):
    with Path(__file__).parent.joinpath('syn.dict').open("rb") as f:
        syn_dict = dict(pickle.load(f))
    kw = []
    for k in keywords:
        w = syn_dict.get(k)
        if w != []:
            kw.extend(w)
            kw.append(k)
    final = df[df['tfidf_score'] >= 0.31]
    purged = df[df['tfidf_score'] <= 0.31]
    rescued = purged[df['text'].astype(str).str.contains('|'.join(kw),case=False)]
    final = pd.concat([final,rescued], ignore_index=True)
    # filtered = final[~(final['text'].astype(str).str.contains('|'.join(keywords),case=False,regex=True))]
    # final = final[final['text'].astype(str).str.contains('|'.join(keywords),case=False,regex=True)]
    final = final.drop('text', axis=1)
    return final.sort_values(by=['tfidf_score'], ascending=False)

# read csv, turn it into a df, removes duplicates
def filtering(df, keywords):
    # df.drop_duplicates(inplace=True) <------------ TO BE DECIDED
    # change title+abstract into a unique column of text
    ## to be analysed separetely
    ## and save it into a column called "text"
    dataset = df.filter(['title','abstract'], axis=1)
    dataset['text'] = df['title'].str.cat(df[['abstract']].astype(str), sep=" ")
    df['text'] = dataset['text']
    # remove stopwords and Nan values
    dataset = nlp.normalize(dataset)
    # change dataset['text'] into a simple list of texts
    texts = dataset['text'].tolist()
    # texts are feed to the model and turned into vectors of words
    vectors = tf_idf.similarity_matrix(texts, keywords)
    # compute similarity scores between text vectors
    ## return a score between 0 and 1
    ## add scores column to original df
    scores = tf_idf.get_scores(len(df),vectors)
    df['tfidf_score'] = scores
    # set a minimum value of similarity
    ## and discard texts that got a score lower than the minimum value
    df = sort_df(df, keywords)
    df.drop('tfidf_score',axis=1) # we don't need to give the score to the client in excel
    return(df)
