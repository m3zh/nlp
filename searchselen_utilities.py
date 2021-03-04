import requests
import clean_utilities as clean
import update_utilities as update
import proxy
from bs4 import BeautifulSoup as bs
import pandas as pd
from torrequest import TorRequest
import time
import random

def search_keywords(keywords, browser, limit):
	#tor = TorRequest(password='meta-a')
	payload = (keywords).replace(' ', '+') # change parameters keyword in url form
	df = [] # creates an empty dataframe
	for i in range(100):
		#p = random.choice(proxies)
		browser.get('https://scholar.google.com/scholar?start={0}&hl=en&as_sdt=0,5&q={1}'.format(i, payload)) #, proxies={"http": p, "https": p})
        # except Exception as e:
		#    print("Bad page request.\nSearch is being terminated after ", i, " results retrieven.")
   	    #    return(df)
		html = browser.page_source
		print("Scarping page {} ...".format(i))
		# if page.status_code != 200:
		# 	print("Bad page request.\nSearch is being terminated after ", i, " results retrieven.")
		# 	return(df)
		html2 = bs(html, "html.parser")
		data = clean.data(html2)
		#tor.reset_identity()
		tmp = pd.DataFrame(data, columns=['Author', 'Title', 'Abstract', 'Year', 'DOI'])
		df.append(tmp)
		time.sleep(1)
		# if i % 4 == 0:
		# 	proxy.update_session(connection, proxies)
	return (df)

def create_df(data):
	df = pd.DataFrame(columns=['Author', 'Title', 'Abstract', 'Year', 'DOI'])
	for d in data:
		df = pd.concat([df, d], ignore_index=True)
	return (df)
