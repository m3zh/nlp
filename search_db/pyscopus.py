from pyscopus import Scopus
import pandas as pd
import sys # needed for import pandas_utils from parent folder
sys.path.append("/..") # needed for import pandas_utils from parent folder
import pandas_utils

def scopus_df_feeder(keywords):
    df= pandas_utils.df_empty_creator() # create empty df

# say Hello to Scopus
    limit= 2000 # max tested = 2000
    apikey = '095547760e767f8b5fdbe548a92316a7' # API KEY
    scopus = Scopus(apikey) #

    search_df = scopus.search("KEY(keywords)", count=limit, view='STANDARD')

    for i in search_df.index:
        df['title']= search_df['title']
        df['publication date']= search_df['cover_date']
        df['journal']= search_df['publication_name']
        df['DOI']= search_df['doi']

    # fill database column
    df['from_database']= 'scopus'
    # apply date time format to publication date column
    df['publication date']= pd.to_datetime(df['publication date'],yearfirst='True')
    return(df)
