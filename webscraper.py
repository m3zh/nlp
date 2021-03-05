import proxy
import search_utilities as s
import update_utilities as update
import selen
from bs4 import BeautifulSoup as bs
import pandas as pd

proxies = proxy.get_started()
connection = proxy.get_session(proxies)
proxy.check_connection(connection)
#enter your search keywords, leaving a space between them, ex.: keyword1 keyword2
data = s.requests_search('africa flowers', proxies, connection, limit=50) #limit -> how many results you want
#doi = update.empty_DOI(doi)


df = s.create_gs_df(data)
df.to_csv('df.csv', sep=',')
df.to_excel('df.xlsx')
#pd.set_option('display.max_colwidth', None)
print(df)
