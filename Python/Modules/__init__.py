#!/bin/python 

import selenium
import shutil
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

# Display Settings Modules 
class Display_Settings:
  def __init__(--display-settings)

  def --display-settings = max(): 
      pd.set_option('display.max_rows', None)

  def --display-settings = 10():
      pd.set_option('display.max_rows', 10)
    
  def --display-settings = 100():
      pd.set_option('display.max_rows', 100)

  def --display-settings = 1000():
      pd.set_option('display.max_rows', 1000)
    
  def --display-settings = 10000():
      pd.set_option('display.max_rows', 10000)
    
