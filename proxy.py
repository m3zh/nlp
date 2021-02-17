import requests
import random
from bs4 import BeautifulSoup as bs
from itertools import cycle
from lxml.html import fromstring
import traceback
from torrequest import TorRequest

def get_started():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = next(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session

def update_session(session, proxies):
    session.proxies.update(proxies) # choose one random proxy
    return session

def check_connection(connection):
	if connection:
		print("Proxy is up and running ...")
	else:
		print("Try another proxy")
		exit()
