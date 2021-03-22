from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests
import sys # needed for import pandas_utils from parent folder
sys.path.append("/..") # needed for import pandas_utils from parent folder
import pandas_utils
from selenium_utils import get_browser
from datetime import datetime
import time
import pandas as pd
import numpy

# FRONTIERSIN FEEDER
def frontiersin_df_feeder(keywords):
    df = pandas_utils.df_empty_creator()
    browser = get_browser()
    browser.get("https://www.frontiersin.org/search?query={0}&tab=articles".format(keywords))
    time.sleep(30) # replace this line by cookies handling
    html1 = browser.page_source
    page1 = bs(html1, "html.parser")

# Start scraping
    test2 = page1.find_all("a", href=True)
    list = []
    for t in test2:
        if 'altmetric' in t['href']:
            list.append(t['href'])

# print each url founded in search page
    # for url in list:
        # print(url)

# Metadata to df
    for count, url in enumerate(list):
        page2 = browser.get(url)
        html2 = browser.page_source # retrieve the page source of the webpage browser is accessing
        page2 = bs(html2, "html.parser")
        try:
            df.at[count, 'title'] = page2.find('td').findNext("div").get_text()
            df.at[count, 'DOI'] = page2.find('td').findNext("a")['href']
            df.at[count, 'abstract'] = page2.find("td").findNext("div").findNext("p").findNext("span").get_text() # not working for full text
            df.at[count, 'abstract'] += page2.find("td").findNext("div").findNext("p").findNext("span").findNext("span").get_text()
            if df.at[count, 'abstract'] == "##":
                df.at[count, 'abstract'] = ""
            df.at[count, 'publication date'] = page2.find("tbody").findNext("tr").findNext("tr").findNext("td").findNext("div").get_text()
            df.at[count, 'publication date'].split(',') # keep date only year
            # add reste to journal
        except AttributeError:
            pass
    df['from_database']= 'frontiersin'
    df.to_csv("./excels/dfFRONTIERSTEST{}.csv".format(datetime.now().time()))
    # df['publication date']= pd.to_datetime(df['publication date'])
    return(df)
