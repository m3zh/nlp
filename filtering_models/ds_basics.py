import re, nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.stem.porter import *
from collections import Counter
import pickle
import numpy as np
from pathlib import Path
# filter results in df by subject
# def check_df(df):
#     keywords = ['engineering','forensic','natural','computer','technology','computing','environmental','information','oncology','chemistry']
#     df = df[~df['journal'].astype(str).str.contains('|'.join(keywords),case=False)]
#     return df

# sort scores, remove scores belowe a min value
# check results and return the final df
def sort_df(df, keyword):
    with Path(__file__).parent.joinpath('syn.dict').open("rb") as f:
        syn_dict = dict(pickle.load(f))
    keywords = syn_dict.get(keyword)
    final = df[~(df['tfidf_score'] <= 0.31)]
    purged = df[~(df['tfidf_score'] >= 0.31)]
    rescued = purged[df['text'].astype(str).str.contains('|'.join(keywords),case=False)]
    purged = purged[~(purged['text'].astype(str).str.contains('|'.join(keywords),case=False))]
    purged = purged.sort_values(by=['tfidf_score'], ascending=False)
    purged.to_csv("purged.csv")
    purged.to_excel("purged.xlsx")
    final = pd.concat([final,rescued], ignore_index=True)
    filtered = final[~(final['text'].astype(str).str.contains('|'.join(keywords),case=False,regex=True))]
    filtered.to_csv("filtered.csv")
    filtered.to_excel("filtered.xlsx")
    final = final[final['text'].astype(str).str.contains('|'.join(keywords),case=False,regex=True)]
    final = final.drop('text', axis=1)
    return final.sort_values(by=['tfidf_score'], ascending=False)
