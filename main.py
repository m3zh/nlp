import tf_idf  # term frequency vectorizer
import numpy as np
import pandas as pd
import nlp_basics as nlp
import ds_basics as ds
from config import KEYWORD


# read csv, turn it into a df, removes duplicates
def main(KEYWORD):
    #global KEYWORD = sys.argv[1]
    df = pd.read_csv('gifted.csv', delimiter=',', usecols=[1,2,3,4,5,6,7,8])
    print(df.shape)
    df.drop_duplicates(inplace=True)
    print(df.shape)
    df = ds.check_df(df) # to change after we add abstracts
    # change title+abstract into a unique column of text
    # to be analysed separetely
    # and save it into a column called "text"
    dataset = df.filter(['title','abstract'], axis=1)
    dataset['text'] = df['title'].str.cat(df[['abstract']].astype(str), sep=" ")
    df['text'] = dataset['text']
    # remove stopwords and Nan values
    dataset = nlp.normalize(dataset)
    # change dataset['text'] into a simple list of texts
    texts = dataset['text'].tolist()
    # texts are feed to the model and turned into vectors of words
    vectors = tf_idf.similarity_matrix(texts)
    # compute similarity scores between text vectors
    # return a score between 0 and 1
    # add scores column to original df
    scores = tf_idf.get_scores(len(df),vectors)
    df['tfidf_score'] = scores
    # set a minimum value of similarity
    # and discard texts that got a score lower than the minimum value
    df = ds.sort_df(df)
    print(df.shape)
    # save the data in csv and xlsl
    df.to_csv("results.csv")
    #df.drop('tfidf_score',axis=1) # we don't need to give the score to the client in excel
    df.to_excel("results.xlsx")
    # to display full-width column in df in terminal
    # pd.set_option('display.max_colwidth', None)
    print(df.shape)

if __name__ == "__main__":
    main(KEYWORD)
