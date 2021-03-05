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
		tmp = pd.DataFrame(data, columns=['title', 'publication_date', 'journal', 'DOI', 'author', 'abstract'])
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
		page = bs(html, "html.parser")
		data = clean.data(page)
		tmp = pd.DataFrame(data, columns=['title', 'publication_date', 'journal', 'DOI', 'author', 'abstract'])
		df.append(tmp)
		time.sleep(1)
	return (df)

def create_gs_df(data):
	df = pd.DataFrame(columns=['title', 'publication_date', 'journal', 'DOI', 'author', 'abstract'])
	for d in data:
		df = pd.concat([df, d], ignore_index=True)
	df.insert(loc=2, column='subject', value="") # no subjects retrieved from google scholar yet
	df['DOI'] = df['DOI'].apply(lambda x: clean.single_DOI(x))
	df['from_database'] = 'gs'
	return (df)
