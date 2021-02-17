import requests
import clean_utilities as clean
import update_utilities as update
from bs4 import BeautifulSoup as bs
import pandas as pd
from torrequest import TorRequest

def keywords(keywords, limit):
	tor = TorRequest(password='meta-a')
	payload = {'q': (keywords).replace(' ', '+') }
	df = pd.DataFrame()
	for i in range(0, limit, 10):
		page = tor.get('https://scholar.google.com/scholar?start={}&hl=en&as_sdt=0,5&'.format(i), params=payload)
		print(page)
		html = bs(page.content, "html.parser")
		data = clean.data(html)
		tor.reset_identity()
		tmp = pd.DataFrame(data, columns=['Author', 'Title', 'Abstract', 'Year', 'DOI'])
		df = pd.concat([df, tmp], ignore_index=True)
	return (df)
