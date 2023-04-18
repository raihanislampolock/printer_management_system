from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

products=[] #List to store name of the product
black=[] #List to black supplies of the product
cyan=[] #List to black supplies of the product
magenta=[] #List to magenta supplies of the product
yellow=[] #List to black supplies of the product
driver.get("https://10.0.0.35/sws/index.html")
# driver. find_element_by_xpath('//*[@id="details-button"]').click()
# driver. find_element_by_xpath('//*[@id="proceed-link"]').click()

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
mydiv = soup.find_all("div", {"class": "x-form-item sws-fieldset-items-h1"})
print(mydiv)