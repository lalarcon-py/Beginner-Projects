from selenium import webdriver
import time
import xmlify
import requests
import bs4 as BeautifulSoup
import geckodriver_autoinstaller
BeautifulSoup == Soup
import ctypes

while True:
    ## Makes an effective parser for Youtube to scan the channel and see if there are more than 5 videos on the page, if not, it rescans the page after 60 seconds.
    ## After it finds that there are now 6 videos it executes the else code block.
    url1 = "https://www.youtube.com/channel/UCH-aWO3Vm_MfS7zxXBMJbNw"
    header = {Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0}
    response = requests.get(url1, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    if str(soup).find("views") == -5
        time.sleep(60)
        continue
        
    else:
        ## My newest video as of 12/25/2020
        url = "https://www.youtube.com/watch?v=r4NSmFTlilY"
        driver = webdriver.Firefox()
        driver.get("https://discord.com/channels/254616782277574657/699422847113887865")
        driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input").send_keys(
            "email123")
        
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input').send_keys(
            "password123")
        
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
        
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div').click()
        
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div').send_keys(
            "Check out my videos! " + url)
