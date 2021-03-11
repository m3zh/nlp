import requests
import random
from bs4 import BeautifulSoup as bs
from itertools import cycle
#from torrequest import TorRequest
import time
from http import cookiejar
from fake_useragent import UserAgent
import multiprocessing as mp

class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

def get_started():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies


def get_session(proxies):
    #ua = UserAgent(cache=False)
    # construct an HTTP session
    session = requests.Session()
    #session.cookies.set_policy(BlockAll())
    #session.headers = ua.random
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session

def update_session(session, proxies):
    #ua = UserAgent(cache=False)
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    #session.headers.update(ua)
    return session

def check_connection(connection):
    if connection:
        print("Proxy is up and running ...")
    else:
        print("Try another proxy")
        exit()
