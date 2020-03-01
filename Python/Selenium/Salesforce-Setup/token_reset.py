#!/bin/python
# ===========================================================
# Created By: Richard Barrett
# Organization: Mirantis
# Department: CSO Support
# Purpose: Reset the Token from CLI
# Date: 03/02/2020
# ===========================================================

import selenium
import shutil
import os
import unittest
import requests
import subprocess
import getpass
import platform
import logging
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from datetime import date

decrypt = "gpg --output secrets_test.json --decrypt secrets.gpg" 

if os.path.exists("secrets.gpg"):
      returned_value = subprocess.call(decrypt, shell=True)
else:
        print("The file does not exist")
            
import json
with open('secrets_test.json','r') as f:
      config = json.load(f)

# Definitions
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# System Variables
today = date.today()
date = today.strftime("%m/%d/%Y")
node = platform.node()
system = platform.system()
username = getpass.getuser()
version = platform.version()

# Check for Version of Chrome

# Options 
options = Options()
options.add_argument("--headless")

# WebDriver Path for System
if platform.system() == ('Windows'):
    browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
elif platform.system() == ('Linux'):
    browser = webdriver.Chrome(executable_path='/home/rbarrett/Drivers/Google/Chrome/chromedriver_linux64/chromedriver')
elif platform.system() == ('Darwin'):
    browser = webdriver(executable_path='~/Drivers/Google/Chrome/chromedriver_mac64/chromedriver')
else:
    print("Are you sure you have the Selenium Webdriver installed in the correct path?")
      
# Parent URL
browser.get("https://mirantis.my.salesforce.com/")

# Credentials NEEDS UNIT TEST
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys(config['user']['username'])
password.send_keys(config['user']['password'])

# UI Container Handle for Notifications Window that Pops Up. 

# Authentication submit.click()
# For XPATH = //*[@id='loginContainer']/form/footer/button
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "Login")))
element.click();
print("Logging into Salesforce Data Center!")

# Navigate to Set-Up
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[2]/div/span")))
element.click();

element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Setup")))
element.click();
print("Entering Salesforce Set-Up.")

# Reset the Salesforce Security Token
# Step 1 - Click Dropdown Menu and Load Current Year Query
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Reset your security token")))
element.click();
print("Your Salesforce Security Token Has Been Reset Check Your Email.")
time.sleep(5)

# Delete the Unencrypted File
if os.path.exists("secrets_test.json"):
  os.remove("secrets_test.json")
  print("The file was removed and everything is clean!")
else:
  print("The file does not exist and encryption is not in use.")

print("The Token Reset was Succesful!")
browser.quit()

# Format Downloaded File to District Specifications
