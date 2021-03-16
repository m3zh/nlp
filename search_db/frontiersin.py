from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import sys # needed for import pandas_utils from parent folder
sys.path.append("/..") # needed for import pandas_utils from parent folder
import pandas_utils
from datetime import datetime
import time


def get_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options) #just changed chrome_options to options to clean warning
    return (browser)

# ajouter function scroll down dans selenium

df = pandas_utils.df_empty_creator()
browser = get_browser()


keywords = "gifted+children+behavior+problems"

page1 = browser.get("https://www.frontiersin.org/search?query={}&tab=articles".format(keywords))
# test= browser.find_elements_by_xpath('//a[contains(@href,"altmetric")]')
time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = browser.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    browser.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = browser.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break

# lnks= browser.find_elements_by_tag_name("a")
# for lnk in lnks:
#    # get_attribute() to get all href
#    print(lnk.get_attribute(href))


html1 = browser.page_source
page1 = BeautifulSoup(html1, "html.parser")
# browser.close()
test2 = page1.find_all("a", href=True)
list = []
for t in test2:
    if 'altmetric' in t['href']:
        list.append(t['href'])
    #ajouter une regex pour ne garder que

for url in list:
    print(url)

for count, url in enumerate(list):
    page2 = browser.get(url)
    html2 = browser.page_source # retrieve the page source of the webpage browser is accessing
    page2 = BeautifulSoup(html2, "html.parser")
    try:
        df.at[count, 'title'] = page2.find('td').findNext("div").get_text()
        df.at[count, 'DOI'] = page2.find('td').findNext("a")['href']
        df.at[count, 'abstract'] = page2.find("td").findNext("div").findNext("p").findNext("span").get_text() # not working for full text
        df.at[count, 'abstract'] += page2.find("td").findNext("div").findNext("p").findNext("span").findNext("span").get_text()
        df.at[count, 'publication date'] = page2.find("tbody").findNext("tr").findNext("tr").findNext("td").findNext("div").get_text()
        df.at[count, 'publication date'].split(',') # keep date only year
        # add reste to journal
    except AttributeError:
        pass

df['from_database']= 'frontiersin'
df.to_csv("./excels/dfFRONTIERSTEST{}.csv".format(datetime.now().time()))
