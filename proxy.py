import requests
import random
from bs4 import BeautifulSoup as bs

def get_free_proxies():
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

proxies = get_free_proxies()

def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session

for i in range(5):
    s = get_session(proxies)
    try:
        print("Request page with IP:", s.get("http://icanhazip.com", timeout=1.5).text.strip())
    except Exception as e:
        continue




# from urllib.request import Request, urlopen
# from fake_useragent import UserAgent
# import random
# from bs4 import BeautifulSoup
# from IPython.core.display import clear_output
#
# # Here I provide some proxies for not getting caught while scraping
# ua = UserAgent() # From here we generate a random user agent
# proxies = [] # Will contain proxies [ip, port]
#
# # Main function
# def main():
#   # Retrieve latest proxies
#   proxies_req = Request('https://www.sslproxies.org/')
#   proxies_req.add_header('User-Agent', ua.random)
#   proxies_doc = urlopen(proxies_req).read().decode('utf8')
#
#   soup = BeautifulSoup(proxies_doc, 'html.parser')
#   proxies_table = soup.find(id='proxylisttable')
#
#   # Save proxies in the array
#   for row in proxies_table.tbody.find_all('tr'):
#     proxies.append({
#       'ip':   row.find_all('td')[0].string,
#       'port': row.find_all('td')[1].string
#     })
#
#   # Choose a random proxy
#   proxy_index = random_proxy()
#   proxy = proxies[proxy_index]
#
#   for n in range(1, 20):
#     req = Request('http://icanhazip.com')
#     req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
#
#     # Every 10 requests, generate a new proxy
#     if n % 10 == 0:
#       proxy_index = random_proxy()
#       proxy = proxies[proxy_index]
#
#     # Make the call
#     try:
#       my_ip = urlopen(req).read().decode('utf8')
#       print('#' + str(n) + ': ' + my_ip)
#       clear_output(wait = True)
#     except: # If error, delete this proxy and find another one
#       del proxies[proxy_index]
#       print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
#       proxy_index = random_proxy()
#       proxy = proxies[proxy_index]
#
# # Retrieve a random index proxy (we need the index to delete it if not working)
# def random_proxy():
#   return random.randint(0, len(proxies) - 1)
#    user_agent = random.choice(user_agent_list)
    # headers= {'User-Agent': user_agent, "Accept-Language": "en-US, en;q=0.5"}
    # proxy = random.choice(proxies)
    # response = get("your url", headers=headers, proxies=proxy)
# if __name__ == '__main__':
#   main()
