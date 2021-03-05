import requests
import clean_utilities as clean
import update_utilities as update
import proxy
from bs4 import BeautifulSoup as bs
import pandas as pd
from torrequest import TorRequest
import time
import random

def requests_search(keywords, proxies, connection, limit):
	#tor = TorRequest(password='meta-a')
	payload = {'q': (keywords).replace(' ', '+') } # change parameters keyword in url form
	df = [] # creates an empty dataframe
	for i in range(0, limit, 10):
		#p = random.choice(proxies)
		page = requests.get('https://scholar.google.com/scholar?start={}&hl=en&as_sdt=0,5&'.format(i), params=payload) #, proxies={"http": p, "https": p})
		print(page)
		if page.status_code != 200:
			print("Bad page request.\nSearch is being terminated after ", i, " results retrieven.")
			return(df)
		html = bs(page.content, "html.parser")
		data = clean.data(html)
		#tor.reset_identity()
		tmp = pd.DataFrame(data, columns=['Author', 'Title', 'Abstract', 'Year', 'DOI'])
		df.append(tmp)
		time.sleep(1)
		if i % 4 == 0:
			proxy.update_session(connection, proxies)
	return (df)

def selenium_search(keywords, browser, limit):
	payload = (keywords).replace(' ', '+') # change parameters keyword in url form
	df = [] # creates an empty dataframe
	for i in range(0, limit, 10):
		browser.get('https://scholar.google.com/scholar?start={0}&hl=en&as_sdt=0,5&q={1}'.format(i, payload)) #, proxies={"http": p, "https": p})
		html = browser.page_source
		print("Scraping page {} ...".format(i // 10))
		html2 = bs(html, "html.parser")
		data = clean.data(html2)
		tmp = pd.DataFrame(data, columns=['Author', 'Title', 'Abstract', 'Year', 'DOI'])
		df.append(tmp)
		time.sleep(1)
	return (df)

def create_df(data):
	df = pd.DataFrame(columns=['Author', 'Title', 'Abstract', 'Year', 'DOI'])
	for d in data:
		df = pd.concat([df, d], ignore_index=True)
	df['DOI'] = df['DOI'].apply(lambda x: clean.single_DOI(x))
	return (df)
