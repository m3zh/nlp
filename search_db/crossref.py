import pandas as pd
from habanero import Crossref

# take an empty DataFrame as argument dataf
## take a string as argument keywords, doesnt handle operators
## feed a DataFrame with results of pubmed database
## doesnt work for authors
def crossref_df_feeder(df, keywords):
    limit= 5
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
                str1 = ', '.join(str(p) for p in p)
                df.at[count, 'publication date'] = str1
            except KeyError:
                pass
        count= count + 1
    df['publication date']= pd.to_datetime(df['publication date'])
    return(df)
