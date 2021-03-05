import proxy
import search_utilities as s
import clean_utilities as clean
import update_utilities as update
import selen
from bs4 import BeautifulSoup as bs
import pandas as pd

browser = selen.get_browser()
#enter your search keywords, leaving a space between them, ex.: keyword1 keyword2
data = s.selenium_search('africa flowers', browser, limit=10) #limit -> how many results you want
#doi = update.empty_DOI(doi)


df = s.create_gs_df(data)
df.to_csv('df.csv', sep=',')
df.to_excel('df.xlsx')
pd.set_option('display.max_colwidth', 25)
print(df)
