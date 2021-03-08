# encoding=utf8
import sys

import time
import os

import requests
import random

from bs4 import BeautifulSoup as soup

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()

options.add_argument("--disable-dev-shm-usage")
#options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Add User Agent option
with open('user_agents.txt','r') as f:
        #f_read = f.read()
        #print(f_read)
    lines = f.readlines()
    #time.sleep(1)
    line = random.choice(lines)
    #print (line)
    user_agent = line.rstrip('\r\n')    
    #print(user_agent)
    #time.sleep(1)
#Check user agent and print
print ("Adding Random User Agent")
#time.sleep(1)
#print (headers) 
test = "user-agent" + "=" + user_agent
#print(test)
options.add_argument(test)
#driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)
#driver.get("https://httpbin.org/user-agent")
print ("Completed")
#time.sleep(1)
#driver.quit()


# Add Proxy option

print ("Adding Proxy")
PROXY = "0000:0000" # IP:PORT or HOST:PORT
options.add_argument('--proxy-server=%s' % PROXY)
#driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)
#driver.get("http://www.privateinternetaccess.com/pages/whats-my-ip/")
print ("Completed")
#time.sleep(1)
#driver.quit()
TESTLINK = "https://www.bestbuy.com/site/compustar-2-way-csx-remote-start-system-lte-module-black/6363155.p?skuId=6363155"
RTX3070LINK1 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
RTX3070LINK2 = "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-8g-gddr6-pci-express-4-0-graphics-card-black/6437912.p?skuId=6437912"
XBOXONETEST = "https://www.bestbuy.com/site/microsoft-xbox-one-s-1tb-console-bundle-white/6415222.p?skuId=6415222"

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)
driver.implicitly_wait(1)
driver.get(TESTLINK)

find_button = driver.find_element_by_class_name('add-to-cart-button')
print (find_button.is_enabled())

find_button.click()

time.sleep(1) # Let the user actually see something!
driver.get("https://www.bestbuy.com/cart")
time.sleep(2) # Let the user actually see something!
driver.quit()