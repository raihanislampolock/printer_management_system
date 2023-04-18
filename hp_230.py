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

def printer_230_details():
    floor_details = {
        "Floor_7_Lab": {
            "url": "http://10.0.1.209/hp/device/info_deviceStatus.html?tab=Home&menu=DevStatus",
            "ip": "10.0.1.209"

        },
        "Floor_3_Fde": {
            "url": "http://10.0.2.145/hp/device/info_deviceStatus.html?tab=Home&menu=DevStatus",
            "ip": "10.0.2.145"
        }

    }

    floor_printer_details = dict()

    for key, val in floor_details.items():
        offline_data = {
          "ip": val["ip"],
          "percentage": {},
          "status": "offline"
        }
        try:
            driver.get(val["url"])
            wait = WebDriverWait(driver, 10)
            content = driver.page_source
            soup = BeautifulSoup(content, features="html.parser")
            mydiv = soup.find_all("td", {"class": "alignRight valignTop"})
            Black = (mydiv[0].get_text().replace("†", "").replace("%", "").strip())
            Drum = (mydiv[1].get_text().replace("†", "").replace("%", "").strip())
            percent = {"black": Black, "drum": Drum}
            floor_printer_details[key] = {
               "ip": val["ip"],
               "percentage": percent,
               "status": "online"
            }
            print(floor_printer_details)

        except Exception as e:
            print(f"Error occurred for {val['url']}: {str(e)}")
            print(traceback.format_exc())
            # send data to the database with an "offline" status
            floor_printer_details[key] = offline_data

    return floor_printer_details
