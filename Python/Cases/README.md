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
    "all_cases_first_response_missed": "ALL_CASES_FIRST_RESPONSE_MISSED_ID",
    "all_cases_handover": "ALL_CASES_HANDOVER_ID",
    "all_cases_sev1": "ALL_CASES_SEV1_ID",
    "all_cases_sev2": "ALL_CASES_SEV2_ID",
    "all_cases_sev3": "ALL_CASES_SEV3_ID",
    "all_cases_sev4": "ALL_CASES_SEV4_ID", 
    "all_cases_sla_violated": "ALL_CASES_SLA_VIOLATED"
  }
}
```

## Locating Salesforce Security Token
Where is the SalesForce Security Token within your SalesForce Organization.
The SlaesForce security token is located within your setup. 
You will probably not even know you have a security token. 
In order to make the Security Token, you will first most likely need to reset your security token within your Salesforce Organizaiton. To do so Navigate to Setup, Click on Reset my Security Token, and you will recieve an email wihin your organization or registered domain that is hosting your corporate email. 

- **[What is Salesforce Security Token and How Do I Find It?](https://www.skyhighnetworks.com/cloud-security-blog/what-is-salesforce-security-token-and-how-do-i-find-it/)**

NEED TO PUT PICTURES AND DOCUMENTATION

## Finding the Salesforce Report ID for A Report 

NEED TO PUT PICTURES AND DOCUMENTATION
