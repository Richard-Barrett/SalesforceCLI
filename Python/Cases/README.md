# Cases
Overall interaction within the Cases tab menu within the SalesForce Service Console can found here. 
The main thing is that a Pandas Dataframe is returned. 

Usage:
```
python read_all_handover_cases.py 
```

## Creating a **`secrets.json`** File
Use a text editor of your choice to make a file. 
Here we use **`vim`** to create the **`secrets.json`** file. 

**Make the File**
```
vim secrets.json
```
Then copy and fill out the following:
```
{
  "user": {
    "username": "INSERT_USERNAME",
    "password": "INSERT_PASSWORD",
    "salesforce_token": "INSERT_TOKEN"
  }
}
```

## Creating a **`reports.json`** File 
Use a text editor of your choice to make a file. 
Here we use **`vim`** to create the **`reports.json`** file. 
```
vim reports.json
```

Then copy and fill out the following:
```
{
  "report": {
    "all_cases": "ALL_CASES_REPORT_ID",
    "all_cases_change_requests": "ALL_CASES_CHANGE_REQUESTS_ID",
    "all_cases_handover": "ALL_CASES_HANDOVER_ID",
    "all_cases_sev1": "ALL_CASES_SEV1_ID",
    "all_cases_sev2": "ALL_CASES_SEV2_ID",
    "all_cases_sev3": "ALL_CASES_SEV3_ID",
    "all_cases_sev4": "ALL_CASES_SEV4_ID"
  }
}
```
## Locating Salesforce Security Token

## Finding the Salesforce Report ID for A Report 
