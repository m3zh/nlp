import proxy
import search_utilities as s
import searchselen_utilities as se
import update_utilities as update
import selen
from bs4 import BeautifulSoup as bs
import pandas as pd

proxies = proxy.get_started()
connection = proxy.get_session(proxies)
proxy.check_connection(connection)
browser = selen.get_browser()
#enter your search keywords, leaving a space between them, ex.: keyword1 keyword2
#data = s.search_keywords('africa flowers', proxies, connection, limit=500) #limit -> how many results you want
data = se.search_keywords('africa flowers', browser, limit=500)
#doi = update.empty_DOI(doi)
df = se.create_df(data)
print(df)
