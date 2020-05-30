import time
from selenium import webdriver

def registration():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(options=options)  # Optional argument, if not specified will search path.
    driver.get('https://twitter.com/i/flow/signup')