from pyscopus import Scopus
import pandas as pd
# needed to import from current folder
import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
sys.path.append("/..") # needed for import pandas_utils from parent folder
import pandas_utils
sys.path.append(".")
from apikeys import scopus_key

def scopus_df_feeder(keywords):
    df = pandas_utils.df_empty_creator() # create empty df

# say Hello to Scopus
    limit = 200 # max tested = 2000
    scopus = Scopus(scopus_key)

    search_df = scopus.search("KEY(keywords)", count=limit, view='STANDARD')

# fill df empty df
    for i in search_df.index:
        df['title'] = search_df['title']
        df['publication date'] = search_df['cover_date']
        df['journal'] = search_df['publication_name']
        df['DOI'] = search_df['doi']

    # fill database column
    df['from_database'] = 'scopus'
    # apply date time format to publication date column
    df['publication date'] = pd.to_datetime(df['publication date'],yearfirst='True')
    return(df)
