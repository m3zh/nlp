import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random
import os
import sys # needed for import pandas_utils from parent folder
sys.path.append("/...") # needed for import pandas_utils from parent folder
import pandas_utils
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import clean_utilities as clean
import selenium_utils

def create_gs_df(keywords, browser, limit):
    payload = (keywords).replace(' ', '+') # change parameters keyword in url form
    df = pandas_utils.df_empty_creator() # create the empty master df
    data = [] # creates a list of data
    for i in range(0, limit, 10): # search results according to a given limit, ecx. limit = 50 results,
        browser.get('https://scholar.google.com/scholar?start={0}&hl=en&as_sdt=0,5&q={1}'.format(i, payload)) # get pages to scrape
        html = bs(browser.page_source, "html.parser") # get html
        page = clean.data(html) # clean html and returns a zipped list ordered by 'title', 'publication date', 'journal', 'DOI', 'author', 'abstract'
        data.append(pd.DataFrame(page, columns=['title', 'publication date', 'journal', 'DOI', 'author', 'abstract'])) # append data in df form to data list
        time.sleep(1) # get some rest before scraping again
    for d in data: # fill in the master df with data
    	df = pd.concat([df, d], ignore_index=True)
    return (df)

# main function, call above and return full df
def gs_df_feeder(keywords):
    # change code to retrieve less than 10 results
    limit = 10 #limit max tested 3000
    browser = selenium_utils.get_browser() # get selenium browser
    df = create_gs_df(keywords, browser, limit=limit) # scrape data and return df
    # fill database column
    df['from_database']= 'google_scholar'
    # apply date time format to publication date column
    df['publication date']= pd.to_datetime(df['publication date'],yearfirst='True') #ValueError: month must be in 1..12
    df.to_csv("newdf.csv")
    return(df)
