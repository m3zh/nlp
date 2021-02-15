from random import choice
import requests
from bs4 import BeautifulSoup

def proxy_generator():
  response = requests.get("https://sslproxies.org/")
  soup = BeautifulSoup(response.content, 'html5lib')
  proxy = {'https': choice(list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))}

  return proxy

def data_scraper(request_method, url, **kwargs):
    while true:
        try:
            proxy = proxy_generator()
            print("Proxy currently being used: {}".format(proxy))
            response = requests.request(request_method, url, proxies=proxy, timeout=7, **kwargs)
            break
            # if the request is successful, no exception is raised
        except:
            print("Connection error, looking for another proxy")
            pass
    return response

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
URL = "https://scholar.google.com/"
PROXY = {"https": "https//59.110.7.190:1080"}

response = requests.get(URL, proxies=PROXY, headers=HEADER)
page_html = response.text
page_soup = soup(page_html, "html.parser")
adresses = page_soup.findAll("li", {"class":"list-group-item"}) #for example

for address in adresses:
    try:
        print(address)
    except (TypeError):
        f.write("invalid data" + "\n")
time.sleep(random.randint(1, 10))
