#!/usr/bin/env python

import selenium
import shutil
import xlsxwriter
import os
import unittest
import requests
import subprocess
import getpass
import platform
import logging
import salesforce_reporting
import simple_salesforce
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from simple_salesforce import Salesforce
from datetime import date
from simple_salesforce import SalesforceLogin

decrypt = "gpg --output secrets.json --decrypt secrets.gpg"

if os.path.exists("secrets.gpg"):
        returned_value = subprocess.call(decrypt, shell=True)
else:
        print("The file does not exist encryption on secrets.json not in use")
#continue

import json
with open('secrets.json','r') as f:
        config = json.load(f)

session_id, instance = SalesforceLogin(
    username = (config['user']['username']),
    password = (config['user']['password']),
    security_token = (config['user']['salesforce_token'])
    )

print(session_id)

# Options
options = Options()
options.add_argument("--headless")
pd.set_option('display.max_rows', None)

# System Variables
today = date.today()
date = today.strftime("%m/%d/%Y")
node = platform.node()
system = platform.system()
username = getpass.getuser()
version = platform.version()

my_sf = salesforce_reporting.Connection((config['user']['username']),
                                        (config['user']['password']),
                                        (config['user']['salesforce_token']))

with open('reports.json','r') as f:
        config = json.load(f)
        
report = my_sf.get_report((config['report']['all_l2_cases']))
parser = salesforce_reporting.ReportParser(report)
report_final = pd.DataFrame(parser.records())
print(report_final)
