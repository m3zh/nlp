import pandas as pd
import nlp_basics as nlp
import topic_modelling as model  # term frequency vectorizer
import numpy as np
from openpyxl.workbook import Workbook

def get_model(df, texts):
    # change texts into vectors of topics
    tmodel, scores = model.topic_matrix(texts)
    # add a new column with the found topic for each subject
    df['topics'] = scores.argmax(axis=1)
    # filter topics according to relevant keywords
    keywords = ['gifted']
    topics = model.filter_topics(tmodel, keywords)
    # filter df by relevant topics
    mask = df['topics'].isin(topics)
    df = df[mask]
    # save df to csv and excel
    df = df.drop('topics', axis=1)
    # df = df.drop('score', axis=1)
    df.to_csv('topic_results.csv')
    # df.drop('topics', axis=1)
    df.to_excel('topic_results.xlsx')
    return (df)

#pd.set_option('display.max_colwidth', None)
# print(topics)
# print(df)
