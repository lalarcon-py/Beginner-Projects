from selenium import webdriver
import geckodriver_autoinstaller
import time
import ctypes
url = 'https://github.com/lalarcon-py'
driver = webdriver.Firefox()
driver.get('https://github.com/lalarcon-py')
soup = BeautifulSoup(response.txt, 'lxml')
updated1 = driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/svg/g/g[47]/rect[7]')
updated2 = driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/svg/g/g[47]/rect[4]')
while updated1 or updated2:
    time.sleep(60)
else:
    ctypes.windll.user32.MessageBoxW(0, "YOU HAVE NOT YET UPDATED YOUR GITHUB PAGE TODAY!!!", "ERROR")
##This program is to provide myself a message to make my daily commits on Github!
