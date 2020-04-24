#!/usr/bin/env python
import argparse
import os
import sys

# Functions for Calling Cases
def sev1():
	os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_sev1_cases.py')

def sev2():
	os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_sev2_cases.py')

def sev3():
        os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_sev3_cases.py')

def sev4():
        os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_sev4_cases.py')

def handover():
        os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_handover_cases.py')

parser = argparse.ArgumentParser(
	description='SalesforceCLI will return Pandas Dataframes from Salesforce Cases within an Organizations SFDC. It will also allow you to interact with Salesforce Lighting Experience or Service console from within the CLI. You will even be able to make leads, create cases, and send off emails all from your CLI!',
	epilog="SalesforceCLI is here to help you automate reports and data within your Organizations SFDC"
)

# Poitional Arguments
#parser.add_argument('accounts', help='Pandas Dataframe that shows all available accounts active within an organizational SFDC')
#parser.add_argument('cases', help='cases dataframes related to defined case report, default is set to all cases')
#parser.add_argument('contacts', help='return a list of contacts as a dataframe')
#parser.add_argument('leads', help='leads dataframes related to all defined leads for user access, default is set to all concurrent leads within an organizational SFDC')
#parser.add_argument('lightning', help='Work with Salesforce Lightning from the CLI')
#parser.add_argument('service', help='Work with Salesforce Service Console from the CLI')
#parser.add_argument('soql', help='SOQL custom query for users within an SFDC')
#parser.add_argument('reports', help='reports dataframes related to defined reporst, default is set to list all available reports for use with SFDC access')

# Optional Arguments
parser.add_argument('-v','--version', action='store_true',
                    help='Returns the version of SalesforceCLI'),
#printf("Optional Arguments for cases")
parser.add_argument('-s1','--sev1', action='store_true',
                    help='Return Pandas Dataframe for all Severity Level 1 Cases'),
parser.add_argument('-s2','--sev2', action='store_true',
                    help='Return Pandas Dataframe for all Severity Level 2 Cases'),
parser.add_argument('-s3','--sev3', action='store_true',
		    help='Return Pandas Dataframe for all Severity Level 3 Cases'),
parser.add_argument('-s4','--sev4', action='store_true',
		    help='Return Pandas Dataframe for all Severity Level 4 Cases'),
parser.add_argument('-ho','--handover', action='store_true',
                    help='Return Pandas Dataframe for all Handover Cases')
args = parser.parse_args()
#args = vars(parser.parse_args())

if args.sev1:
   	os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_sev1_cases.py')

if args.sev2:
	os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_sev2_cases.py')

if args.sev3:
        os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_sev3_cases.py')

if args.sev4:
        os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_sev4_cases.py')

if args.handover:
        os.system('python3 ~/Git/SalesforceCLI/Python/Cases/read_all_handover_cases.py')
