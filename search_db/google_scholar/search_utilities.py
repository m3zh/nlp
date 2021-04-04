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
import search_utilities as s

def selenium_search(keywords, browser, limit):
	payload = (keywords).replace(' ', '+') # change parameters keyword in url form
	df = [] # creates an empty dataframe
	for i in range(0, limit, 10):
		browser.get('https://scholar.google.com/scholar?start={0}&hl=en&as_sdt=0,5&q={1}'.format(i, payload)) #, proxies={"http": p, "https": p})
		html = browser.page_source
		page = bs(html, "html.parser")
		data = clean.data(page)
		tmp = pd.DataFrame(data, columns=['title', 'publication date', 'journal', 'DOI', 'author', 'abstract'])
		df.append(tmp)
		time.sleep(1)
	return (df)

# create empty df
## concat line per line data from selenium_search
def create_gs_df(data):
	df = pandas_utils.df_empty_creator()
	for d in data:
		df = pd.concat([df, d], ignore_index=True)
	return (df)

# main function, call above and return full df
def gs_df_feeder(keywords):
    # change code to retrieve less than 10 results
    limit = 3000 #limit max tested 3000
    browser = selenium_utils.get_browser()
    data = s.selenium_search(keywords, browser, limit=limit)
    df = s.create_gs_df(data)

    # fill database column
    df['from_database']= 'google_scholar'
    # apply date time format to publication date column
    df['publication date']= pd.to_datetime(df['publication date'],yearfirst='True') #ValueError: month must be in 1..12
    return(df)
