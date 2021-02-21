import proxy
import search_utilities as search
import update_utilities as update
from bs4 import BeautifulSoup as bs
import pandas as pd

proxies = proxy.get_started()
#connection = proxy.get_session(proxies)
#proxy.check_connection(connection)

#enter your search keywords, leaving a space between them, ex.: keyword1 keyword2
df = search.keywords('africa plants', limit=150) #limit -> how many results you want
#doi = update.empty_DOI(doi)
print(df)
