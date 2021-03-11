import pandas as pd
import numpy as np
from habanero import Crossref
import sys # needed for import pandas_utils from parent folder
sys.path.append("/..") # needed for import pandas_utils from parent folder
import pandas_utils

# take an empty DataFrame as argument dataf
## take a string as argument keywords, doesnt handle operators
## feed a DataFrame with results of pubmed database
## doesnt work for authors
## var limit up to 1000 on 2021-02-21
def crossref_df_feeder(keywords):
    # # create empty df
    df= pandas_utils.df_empty_creator()

    limit= 1 #limit tested = 1000
    cr= Crossref()
    Crossref(mailto= "fool@gmail.com")

    # search in database
    ## return fields selection in a list, fields allowed for selection are :
    ## abstract, URL, member, posted, score, created,
    ## degree, update-policy, short-title, license, ISSN, container-title, issued, update-to,
    ## issue, prefix, approved, indexed, article-number, clinical-trial-number, accepted, author,
    ## group-title, DOI, is-referenced-by-count, updated-by, event, chair, standards-body, original-title,
    ## funder, translator, archive, published-print, alternative-id, subject, subtitle, published-online,
    ## publisher-location, content-domain, reference, title, link, type, ##publisher, volume, references-count,
    ## ISBN, issn-type, assertion, deposited, page, content-created, short-container-title, relation, editor
    res= cr.works(query= keywords, limit= limit, select= ["title","DOI","author", "abstract", "published-print", "subject"], sort ="published")

    # dataframe feeder
    ## work for title, DOI, abstract
    count= 0
    fields= res['message']['items'][count].keys()
    while (count < limit):
        for t in res['message']['items'][count]['title']:
            try:
                df.at[count, 'title']= t
            except KeyError:
                pass
        if 'DOI' in fields:
            try:
                df.at[count, 'DOI']= res['message']['items'][count]['DOI']
            except KeyError:
                pass
        if 'abstract' in res['message']['items'][count]:
            try:
                df.at[count, 'abstract']= res['message']['items'][count]['abstract']
            except KeyError:
                pass
        if 'published-print' in fields:
            try:
                p= res['message']['items'][count]['published-print']['date-parts'][0]
                str1= ', '.join(str(p) for p in p)
                df.at[count, 'publication date']= str1
            except KeyError:
                pass
        if 'subject' in res['message']['items'][count]:
            try:
                df.at[count, 'subject']= res['message']['items'][count]['subject'][0]
            except KeyError:
                pass
        if 'author' in res['message']['items'][count]:
            try:
                df.at[count, 'author']= res['message']['items'][count]['author'][0]
            except KeyError:
                pass
        count= count + 1
    # fill database column
    df['from_database']= 'crossref'
    # apply date time format to publication date column
    df['publication date']= pd.to_datetime(df['publication date'])
    return(df)
