#!/bin/usr/env python
import gspread
import json
import requests
import os
import platform
from oauth2client.service_account import ServiceAccountCredentials

decrypt = "gpg --output secrets.json --decrypt secrets.gpg"

if os.path.exists("secrets.gpg"):
      returned_value = subprocess.call(decrypt, shell=True)
else:
        print("The file does not exist")

with open('secrets.json','r') as f:
      config = json.load(f)

# Example:
# use creds to create a client to interact with the Google Drive API
# scope = ['https://spreadsheets.google.com/feeds']
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
# sheet = client.open("Copy of Legislators 2017").sheet1

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

scope = [(config['google_sheets']['sheets_1']['sheets_url'])]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open(config['google_sheets']['sheets_1']['sheets_name']).sheet1
list_of_hashes = pd.DataFrame(sheet.get_all_records())
print(list_of_hashes)
