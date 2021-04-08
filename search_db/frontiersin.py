from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import org.openqa.selenium.JavascriptExecutor;
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
    time.sleep(10) # replace this line by cookies handling
    last = ''
    while True:
        elem = "#article-results > ul > li:last-child" # gets the last article result of the page so far
        scroll = "document.querySelector(\'" + elem + "\').scrollIntoView();" # scroll the View up to the last article
        browser.execute_script(scroll) # execute the js scroll
        # increase time.sleep if you get 'javascript error: Cannot read property 'scrollIntoView' of null' /no results are retrieved/your connection is slow
        time.sleep(3)  # <-- this is the time the page needs to load the new results;
        # keep scrolling until current element is the same as previous page last element
        if last != elem:
            last = elem
        else:
            break


    # gets all a.href through javascript
    js_script = '''\
    var links = []
    document.querySelectorAll('a').forEach(a => links.push(a.href));
    return links;
    '''
    links = browser.execute_script(js_script)
    # keeps only a.href with a doi
    url_list = []
    for l in links:
        if 'altmetric' in l:
            url_list.append(l)

    # Metadata to df
    for count, url in enumerate(url_list):
        page2 = browser.get(url)
        html2 = browser.page_source # retrieve the page source of the webpage browser is accessing
        page2 = bs(html2, "html.parser")
        try:
            df.at[count, 'title'] = page2.find('td').findNext("div").get_text()
            df.at[count, 'DOI'] = page2.find('td').findNext("a")['href']
            df.at[count, 'abstract'] = page2.find("td").findNext("div").findNext("p").findNext("span").get_text() # not working for full text
            # df.at[count, 'abstract'] += page2.find("td").findNext("div").findNext("p").findNext("span").findNext("span").get_text()
            if df.at[count, 'abstract'] == "##":
                df.at[count, 'abstract'] = ""
            date_and_journal = page2.find("tbody").findNext("tr").findNext("tr").findNext("td").findNext("div").get_text().split(',')
            df.at[count, 'publication date'] = date_and_journal[1]
            df.at[count, 'journal'] = date_and_journal[0]
            # keep date only year
            # add reste to journal
        except AttributeError:
            pass

    df['from_database'] = 'frontiersin'
    df.to_csv("./excels/dfFRONTIERSTEST{}.csv".format(datetime.now().time()))
    # df['publication date']= pd.to_datetime(df['publication date'])
    browser.close()
    return(df)
