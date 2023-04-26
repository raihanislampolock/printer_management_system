from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests
import traceback
import sys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def printer_508_details():
    floor_details = {
        "Floor_1_Deo_Colour": {
            "url": "http://10.1.0.247/",
            "ip": "10.1.0.247"
        },

        "Floor_3_Deo_Colour": {
            "url": "http://10.0.0.230/",
            "ip": "10.0.0.230"
        },

        "Floor_4_Fde_Colour": {
            "url": "http://10.1.0.243/",
            "ip": "10.1.0.243"
        },

        "Floor_9_Corporate_Colour": {
            "url": "http://10.1.0.241/",
            "ip": "10.1.0.241"
        },
    }

    floor_printer_details = dict()

    for key, val in floor_details.items():
        try:
            driver.get(val["url"])
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="details-button"]')))
            element.click()
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="proceed-link"]')))
            element.click()

            content = driver.page_source
            soup = BeautifulSoup(content, features="html.parser")

            mydiv = soup.find_all("div", {"class": "consumable"})
            message_div = soup.find("span", {"id": "MachineStatus"})
            color = soup.find_all("h2")

            count = 0
            colours = dict()
            for item in range(len(mydiv) - 1):
                pinter_name = mydiv[count].findNext("h2").get_text()
                colour_percentage = mydiv[count].findNext("span").get_text().strip("*")
                colours[pinter_name] = colour_percentage
                count += 1

            floor_printer_details[key] = {
                "ip": val["ip"],
                "percentage": colours,
                "status": "online",
                "device_status": message_div.get_text()
            }

        except Exception as e:
            print(f"Error occurred for {val['url']}: {str(e)}")
            print(traceback.format_exc())
            # send data to the database with an "offline" status
            offline_data = {
                "ip": val["ip"],
                "percentage": {},
                "status": "offline",
                "device_status": "Offline"
            }
            floor_printer_details[key] = offline_data

    return floor_printer_details

# print(printer_508_details())