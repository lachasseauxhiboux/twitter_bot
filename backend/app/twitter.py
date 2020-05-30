import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app.sms_service import get_number


def registration():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(options=options)  # Optional argument, if not specified will search path.
    driver.get('https://twitter.com/i/flow/signup')
    username = 'Test'
    phonenumber = get_number()
    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        phone_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "phone_number"))
        )
        username_field.send_keys(username)
        phone_field.send_keys(phonenumber)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[(contains(@role, 'button'))and div][not(@disabled)]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Next']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='Sign up']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='OK']"))
        ).click()
    finally:
        time.sleep(5)


registration()
