from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import proxy
import random

def get_browser():
    # req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
    # proxies = req_proxy.get_proxy_list() #this will create proxy list
    # PROXY = proxies[random.randrange(len(proxies))].get_address()
    #PROXY = proxy.get_started()[random.randrange(200)]
    #print(PROXY)
    # webdriver.DesiredCapabilities.CHROME['proxy']={
    #     "httpProxy":PROXY,
    #     "ftpProxy":PROXY,
    #     "sslProxy":PROXY,
    #     "proxyType":"MANUAL",
    # }
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    #options.add_argument('--proxy-server=http://'+PROXY)
    options.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=options)
    return (browser)
#assert 'google' in browser.title

# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
#
# browser.quit()
