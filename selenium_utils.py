from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    # options.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=options)
    return (browser)
