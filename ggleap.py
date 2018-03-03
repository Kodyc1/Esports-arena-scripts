''' DEPENDENCIES'''
# pip install -U selenium
# install chrome driver 


import time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import bs4
import urllib


# Chrome Driver
browser = webdriver.Chrome(executable_path="C:\Python35\selenium\webdriver\chromedriver_win32\chromedriver.exe")
# Log in to admin
''' TODO: NEED TO ENCRYPT USERNAME AND PASSWORD '''
browser.get("https://USERNAME:PASSWORD@admin.ggleap.com/")

# Log in to ggleap
''' TODO: NEED TO ENCRYPT USERNAME AND PASSWORD '''
username = browser.find_element_by_css_selector("input[ngcontrol='username']")
username.send_keys("USERNAME")

password = browser.find_element_by_css_selector("input[ngcontrol='password']")
password.send_keys("PASSWORD")

browser.find_element_by_css_selector(".btn.btn-primary").click()

time.sleep(10)
action = action_chains.ActionChains(browser)
action.send_keys(Keys.ESCAPE)
action.perform()




browser.get('https://admin.ggleap.com/computers')

time.sleep(30)

block = browser.page_source
        
soup = bs4.BeautifulSoup(block, 'html.parser')

print(len(soup.findAll('td', text="Occupied")))

    
