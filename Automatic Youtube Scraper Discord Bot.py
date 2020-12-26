import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
import xmlify
import requests
import pandas as pd
import json
import os
import bs4 as BeautifulSoup
BeautifulSoup == Soup
## My newest video as of 12/25/2020
url = "https://www.youtube.com/watch?v=r4NSmFTlilY"
driver = webdriver.Firefox()
driver.get("https://discord.com/channels/254616782277574657/699422847113887865")
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input").send_keys("email123@email.com")
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input').send_keys("Password123")
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div').click()
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div').send_keys("Check out my videos! " + url)
while True:
    url = "https://www.youtube.com/channel/UCH-aWO3Vm_MfS7zxXBMJbNw"
    header = {Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    soup.title






