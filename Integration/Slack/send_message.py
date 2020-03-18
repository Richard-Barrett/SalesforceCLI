#!/bin/python
# ===========================================================
# Created By: Richard Barrett
# Organization: Mirantis
# Department: Customer Success Operation
# Purpose: Send Message to Slack Channel 
# Date: 03/18/2020
# ===========================================================

import shutil
import os
import unittest
import requests
import subprocess
import getpass
import platform
import logging
import time 
from datetime import date
import json
from slackclient import SlackClient

decrypt = "gpg --output secrets.json --decrypt secrets.gpg" 

if os.path.exists("secrets.gpg"):
      returned_value = subprocess.call(decrypt, shell=True)
else:
        print("The file does not exist")
            
with open('secrets.json','r') as f:
      config = json.load(f)

# System Variables
date = today.strftime("%m/%d/%Y")
now = datetime.now()
today = date.today()
current_directory = os.getcwd()
node = platform.node()
system = platform.system()
username = getpass.getuser()
version = platform.version()

# Slack Sessions
slack_token = os.environ(config['slack_config']['slack_api_token'])
sc = SlackClient(slack_token)

# Example Calls
#sc.api_call(
#  "chat.postMessage",
#  channel="#python",
#  text="Hello from Python! :tada:"
#)

sc.api_call(
  "chat.postMessage",
  channel = "(config['slack_destination']['channel'])",
  text = "(config['slack_message']['message'])"
)

print("Message Has Posted")
