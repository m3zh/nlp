import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import search_utilities as s
import selen
import pandas as pd
sys.path.append("/../../..") # needed for import pandas_utils from parent folder
import pandas_utils

def gs_df_feeder(keywords):

    #df= pandas_utils.df_empty_creator()
    
    # change code to retrieve less than 10 results
    limit= 3 #limit max 3000
    browser = selen.get_browser()
    data = s.selenium_search(keywords, browser, limit=limit)
    df = s.create_gs_df(data)

    # fill database column
    df['from_database']= 'google_scholar'
    # apply date time format to publication date column
    df['publication date']= pd.to_datetime(df['publication date'],yearfirst='True')
    return(df)
