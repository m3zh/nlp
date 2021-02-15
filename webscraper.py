import requests
import random
import proxy
import clean_utilities as clean
from bs4 import BeautifulSoup as bs
import sys
import pandas as pd

proxies = proxy.get_started()
search = proxy.get_session(proxies)

if search:
	print("Proxy is up and running ...")
else:
	print("Try another proxy")
	exit()

payload = {'q': 'depression+cannabis'} # to add more keywords add +word
page = requests.get('https://scholar.google.com/scholar?hl=en&q=', params=payload)
soup = bs(page.content, "html.parser")
titles = soup.find_all('h3', class_='gs_rt')
authors = soup.find_all('div', class_='gs_a')

titles = clean.my_text(titles)
authors = clean.my_text(authors)
abstracts = clean.my_text(abstracts)

data = list(zip(authors, titles, abstracts))
df = pd.DataFrame(data, columns=['Author', 'Title', 'Abstract'])
print(df)
