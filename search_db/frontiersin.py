from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests
import sys # needed for import pandas_utils from parent folder
sys.path.append("/..") # needed for import pandas_utils from parent folder
import pandas_utils

def get_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options) #just changed chrome_options to options to clean warning
    return (browser)


df = pandas_utils.df_empty_creator()
browser = get_browser()


keywords = "gifted+children+behavior+problems"

page1 = browser.get("https://www.frontiersin.org/search?query={}&tab=articles".format(keywords))
# test= browser.find_elements_by_xpath('//a[contains(@href,"altmetric")]')


# lnks= browser.find_elements_by_tag_name("a")
# for lnk in lnks:
#    # get_attribute() to get all href
#    print(lnk.get_attribute(href))


html1 = browser.page_source
page1 = bs(html1, "html.parser")
# browser.close()

test2 = page1.find_all("a", href=True)
list = []
for t in test2:
    if 'altmetric' in t['href']:
        list.append(t['href'])
    #ajouter une regex pour ne garder que
print(list)

for url in list:
    page2 = browser.get(url)
    html2 = browser.page_source # retrieve the page source of the webpage browser is accessing
    page2 = bs(html2, "html.parser")
    #OK print(page2)
    ths = page2.find_all("th")
    print(ths)
    for th in ths:
        if 'Title' in th:
            print(th["Title"])
    # print(page2)
    # page2.type()
    # title= page2.find_all("th", td=True)#title to df
    # df['title']+= title
    # test4= page2.find("td", text="Title")
    # .find_next_sibling("td").text
    # DOI
    #abstarct
    #published in

# display(df)


# print(test4)
#on veut tous les trucs de l'id articles-results
# chopper les liens altmetric et retrieve de là les infos
# ajouter function scroll down dans selenium
