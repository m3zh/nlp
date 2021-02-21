import requests
import random
from bs4 import BeautifulSoup as bs
from itertools import cycle
from lxml.html import fromstring
import traceback
from torrequest import TorRequest
import time
from http import cookiejar
from fake_useragent import UserAgent
import multiprocessing as mp

class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

def get_started():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = []
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.append(proxy)
    return proxies

def get_session(proxies):
    #ua = UserAgent(cache=False)
    # construct an HTTP session
    session = requests.Session()
    #session.cookies.set_policy(BlockAll())
    #session.headers = ua.random
    proxy = next(iter(proxies))
    session.proxies = {"http": proxy, "https": proxy}
    return session

def update_session(proxies):
    #ua = UserAgent(cache=False)
    session = requests.Session()
    session.proxies.update(proxies)
    #session.headers.update(ua)
    time.sleep(1)
    return session

def check_connection(connection):
    if connection:
        print("Proxy is up and running ...")
    else:
        print("Try another proxy")
        exit()
