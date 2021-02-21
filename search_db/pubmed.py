from Bio import Entrez
import re
import pandas as pd

# take an empty DataFrame as argument df
## take a string as argument keywords, handle operators
## feed a DataFrame with results of pubmed database
## doesnt work for authors
def pubmed_df_feeder(df, keywords):
    # say hello to NCBI.gov
    Entrez.email= 'monAdresse@mail.com'
    Entrez.tool= 'monScript'

    # search in database
    limit= 100
    handle= Entrez.esearch(db= 'pubmed', term= keywords, retmax= limit)
    tmp= Entrez.read(handle)
    id_list= tmp['IdList']
    handle= Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="xml")
    records= Entrez.read(handle); handle.close()

    # dataframe feeder
    ## work for title, DOI, abstract
    count= 0
    while (count < limit):
        for record in records["PubmedArticle"]:
            df.at[count, 'title']= record["MedlineCitation"]["Article"]["ArticleTitle"]
            try:
                df.at[count, 'DOI']= record["MedlineCitation"]["Article"]['ELocationID'][0]
            except IndexError:
                pass
            try:
                df.at[count, 'abstract']= record["MedlineCitation"]["Article"]["Abstract"]["AbstractText"][0]
            except KeyError:
                pass
            df.at[count, 'journal']= record["MedlineCitation"]["Article"]["Journal"]['Title']
            try:
                df.at[count, 'publication date']= record["MedlineCitation"]["Article"]["ArticleDate"][0]['Year']
                df.at[count, 'publication date']+= " "
                df.at[count, 'publication date']+= record["MedlineCitation"]["Article"]["ArticleDate"][0]['Month']
                df.at[count, 'publication date']+= " "
                df.at[count, 'publication date']+= record["MedlineCitation"]["Article"]["ArticleDate"][0]['Day']
            except IndexError:
                pass
            # try:
            #     df.at[count, ""]= record["MedlineCitation"]["Article"]["AuthorList"][0]
            # except ValueError:
            #     pass
        count= count +1
    df['publication date']= pd.to_datetime(df['publication date'],yearfirst='True')
    return(df)