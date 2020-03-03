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

By Default, SalesForce does not actually expose this so you have to reset your Token if you do not know it. 
You can request a Token Reset by following the below steps:


- **Navigate to Set-Up**
![Navigate to Set-Up](https://uploads.skyhighnetworks.com/2016/09/21134631/sfdc-security-token-image-2.1.png)

- **Click on Set-Up and Move to the Next Page and Request to Reset Security Token**
![Request Reset](https://uploads.skyhighnetworks.com/2016/09/21134650/sfdc-security-token-image-3.1.png)


## Finding the Salesforce Report ID for A Report 
To get the report of a Salesforce Report ID you will need to first make sure that it follows certain conventions.

- 1. It cannot be a Personal Report
- 2. The Report Must be Saved in a Shared Folder 
- 3. The Report must be ran. 

The ID of a Report can be found by looking at the end of the URL. 
Look at the following pictures to understand where to locate the report ID.
You can find the ID for the Report after you have created it. 
To so navigate to the top right hand corner of your SalesForce view and click the down arrow. 

- **Navigate to the Down Arrow Underneath Profile Image in the Reports Tab**
![Image](https://triking-creative.s3.amazonaws.com/Logos/SalesforceCLI/Documentation/Salesforce_Report_ID_Locate_A_Arrows.PNG)

After clicking on the Icon Link a pop window will appear.
This window will share a link with the root part of the directory being your salesforce domain name. 
The second part will be a string containing a unique ID for the report. 
This is the report ID.

- **Click on The Link Icon to See The Shareable Link**
![Image](https://triking-creative.s3.amazonaws.com/Logos/SalesforceCLI/Documentation/Salesforce_Report_ID_Locate_B_Arrows.PNG)
