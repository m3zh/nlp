from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import proxy

def get_browser():
    # req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
    # proxies = req_proxy.get_proxy_list() #this will create proxy list
    # PROXY = proxies[0].get_address()
    # #PROXY = proxy.get_started()[0]
    # webdriver.DesiredCapabilities.CHROME['proxy']={
    #     "httpProxy":PROXY,
    #     "ftpProxy":PROXY,
    #     "sslProxy":PROXY,
    #     "proxyType":"MANUAL",
    # }
    options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--incognito')
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options)
    return (browser)
#assert 'google' in browser.title

# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
#
# browser.quit()
