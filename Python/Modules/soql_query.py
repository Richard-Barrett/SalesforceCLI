from pandas import DataFrame
from simple_salesforce import SalesforceAPI
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

# Function to Return Salesforce SOQL Queries as Dataframes
# =========================================================
def sql_query(query_str):
    qry_result = sf.query(query_str)
    print('Record Count {0}'.format(qry_result['totalSize']))
    is_done = qry_result['done']
    if is_done:
        df = DataFrame(qry_result['records'])
    while not is_done:
        try:
            if not qry_result['done']:
                df = df.append(DataFrame(qry_result['records']))
                qry_result = sf.query_more(qry_result['nextRecordsUrl'], True)
            else:
                df = df.append(DataFrame(qry_result['records']))
                is_done = True
                print('completed')
                break
        except NameError:
            df = DataFrame(qry_result['records'])
            sf.query_more(qry_result['nextRecordsUrl'], True)
    df = df.drop('attributes', axis=1)
    return df

soql_test = 'SELECT Milestone_violated__c, First_Reply__c, CaseNumber, Environment2__r.Name,' \
            ' Owner.Name, Severity_Level__c, Status, Subject, URL_for_support__c from Case'

res = sql_query(soql_test)
print(res)
