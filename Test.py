#import pytest
import time
#import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from config import *
browser = webdriver.Firefox()

browser.get(URL_TO_TEST)
assert 'OrangeHRM' in browser.title
browser.maximize_window()

def login(username, password):
    """Documentación:
    Esta funcion recibe como parametros el usuario y la contraseña para realizar el ingreso a la pagina."""
    time.sleep(TIME_SECONDS_SHORT)
    browser.find_element(By.NAME, "username").send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, ".oxd-button").click()

def recruit(firstName, middleName, lastName, jobVacancy, email, filePath, contactNumber, keywords, notes):
    """Documentación:+
    Esta funcion recibe como parametros los datos del aspirante e inicia el proceso de reclutamiento."""
    time.sleep(TIME_SECONDS_SHORT)
    browser.find_element(By.CSS_SELECTOR, "li.oxd-main-menu-item-wrapper:nth-child(5) > a:nth-child(1)").click()
    time.sleep(TIME_SECONDS_SHORT)
    browser.find_element(By.XPATH, "//button[@type='button'][contains(.,'Add')]").click()
    time.sleep(TIME_SECONDS_SHORT)
    browser.find_element(By.NAME, "firstName").click()
    browser.find_element(By.NAME, "firstName").send_keys(firstName)
    browser.find_element(By.NAME, "middleName").click()
    browser.find_element(By.NAME, "middleName").send_keys(middleName)
    browser.find_element(By.NAME, "lastName").click()
    browser.find_element(By.NAME, "lastName").send_keys(lastName)
    browser.find_element(By.CSS_SELECTOR, ".oxd-select-text-input").send_keys(jobVacancy)
    browser.find_element(By.CSS_SELECTOR, "div.oxd-form-row:nth-child(2) > div:nth-child(1)").click()
    browser.find_element(By.CSS_SELECTOR, "div.oxd-form-row:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").click()
    browser.find_element(By.CSS_SELECTOR, "div.oxd-form-row:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys(email)
    browser.find_element(By.CSS_SELECTOR, ".oxd-file-input").send_keys(filePath)
    browser.find_element(By.CSS_SELECTOR, "div.oxd-form-row:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").click()
    browser.find_element(By.CSS_SELECTOR, "div.oxd-form-row:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys(contactNumber)
    browser.find_element(By.CSS_SELECTOR, "div.oxd-form-row:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").click()
    browser.find_element(By.CSS_SELECTOR, "div.oxd-form-row:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys(keywords)
    browser.find_element(By.CSS_SELECTOR,".oxd-textarea").click()
    browser.find_element(By.CSS_SELECTOR,".oxd-textarea").send_keys(notes)
    browser.find_element(By.CSS_SELECTOR, ".bi-check").click()
    browser.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
    time.sleep(TIME_SECONDS_MEDIUM)
    browser.find_element(By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item'][contains(.,'Candidates')]").click()

login(USER_NAME, PASSWORD)
recruit(FIRST_NAME, MIDDLE_NAME, LAST_NAME, JOB_VACANCY, EMAIL, FILE_PATH, CONTAC_NUMBER, KEYWORDS, NOTES)
time.sleep(TIME_SECONDS_LONG)
browser.quit()