# from bs4 import BeautifulSoup
# # from urllib.request import urlopen
# #
# # url = "http://olympus.realpython.org/profiles/dionysus"
# # page = urlopen(url)
# # html = page.read().decode("utf-8")
# # soup = BeautifulSoup(html, "html.parser")
#
# import requests
#
# proxies = {"http": "http://10.10.1.10:3128",
#            "https": "http://10.10.1.10:1080"}
# header = {
# 		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
# 	}
#
# requests.get("http://example.org", proxies=proxies,headers=header)
#print(response.content)

from bs4 import BeautifulSoup
import requests
from random import randrange

proxies = []
def LoadUpProxies():
	url='https://sslproxies.org/'
	header = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
	}
	response=requests.get(url,headers=header)
	soup=BeautifulSoup(response.content, 'lxml')
	for item in soup.select('#proxylisttable tr'):
		try:
			proxies.append({'ip': item.select('td')[0].get_text(), 'port': item.select('td')[1].get_text()})
		except:
			print('')
LoadUpProxies()
rnd=randrange(len(proxies))
randomIP=proxies[rnd]['ip']
randomPort=proxies[rnd]['port']
print(randomIP)
print(randomPort)
