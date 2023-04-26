from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import requests
import sys
import traceback

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def printer_brother_details():
    # floor_details = dict()
    floor_details = {
        "Floor_1_Fde": {
            "url": "http://10.1.0.248/general/status.html",
            "ip": "10.1.0.248"
        },
        "Floor_2_Fde": {
            "url": "http://10.1.0.250/general/status.html",
            "ip": "10.1.0.250"
        },
        "Floor_2_Nurse": {
            "url": "http://10.1.0.251/general/status.html",
            "ip": "10.1.0.251"
        },
        "Floor_3_Deo": {
            "url": "http://10.0.0.226/general/status.html",
            "ip": "10.0.0.226"
        },
        "Floor_4_Nurse": {
            "url": "http://10.1.0.245/general/status.html",
            "ip": "10.1.0.245"
        },
        "Floor_5_Fde": {
            "url": "http://10.1.0.246/general/status.html",
            "ip": "10.1.0.246"
        },
        "Floor_6_Fde": {
            "url": "http://10.0.4.171/general/status.html",
            "ip": "10.0.4.171"
        },
        "Floor_8_Lab": {
            "url": "http://10.0.4.134/general/status.html",
            "ip": "10.0.4.134"
        },
        "Floor_8_Corporate": {
            "url": "http://10.1.0.242/general/status.html",
            "ip": "10.1.0.242"
        },
        "Floor_9_Corporate": {
            "url": "http://10.1.0.240/general/status.html",
            "ip": "10.1.0.240"
        }
    }

    floor_printer_details = dict()

    for key, val in floor_details.items():
        offline_data = {
          "ip": val["ip"],
          "percentage": {},
          "status": "offline",
          "device_status": "Offline"
        }

        try:
            driver.get(val["url"])
            wait = WebDriverWait(driver, 10)
            content = driver.page_source
            soup = BeautifulSoup(content, features="html.parser")
            mydiv = soup.find("img", {"class": "tonerremain"})
            mydiv2 = soup.find_all("span", {"class": "moni moniOk"})

            height = int(mydiv['height'])
            quotient = height / 56
            perc = int(quotient * 100)

            percent = {"black": perc}
            for span in mydiv2:
                span_text = span.text

            floor_printer_details[key] = {
                "ip": val["ip"],
                "percentage": percent,
                "status": "online",
                "device_status": span_text
            }

        except Exception as e:
            print(f"Error occurred for {val['url']}: {str(e)}")
            print(traceback.format_exc())
            # send data to the database with an "offline" status
            floor_printer_details[key] = offline_data

    return floor_printer_details
