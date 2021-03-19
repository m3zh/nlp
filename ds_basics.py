import re, nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.stem.porter import *
from collections import Counter

# filter results in df by subject
def check_df(df):
    keywords = ['engineering','forensic','natural','computer','technology','computing','environmental','information']
    df = df[~df['journal'].astype(str).str.contains('|'.join(keywords),case=False)]
    return df

# sort scores, remove scores belowe a min value
# check results and return the final df
def sort_df(df):
    keywords = ["gifted"]
    final = df[~(df['score'] <= 0.31)]
    purged = df[~(df['score'] >= 0.31)]
    rescued = purged[df['title'].astype(str).str.contains('|'.join(keywords),case=False)]
    final = pd.concat([final,rescued], ignore_index=True)
    final = final.sort_values(by=['score'], ascending=False)
    return final
