## Python
![Image](https://www.python.org/static/img/python-logo@2x.png)

Python was chosen in mind to help create an overall CLI tool that would allw people to pull out information regarding their Salesforce interactions. The main modules used are listed below:

- **[Simple-Salesforce](https://pypi.org/project/simple-salesforce/)**
- **[Salesforce-Reporting](https://pypi.org/project/salesforce-reporting/)**

The main reason as to why these two modules were chosen is because Salesforce stores things in terms of Objects. Furthermore, they the output returned is in JSON Format from a SQL Query. SalesForce calls this Salesforce Object Query Language, however the structure is very similar to SQL Statements similar to a SELECT FROM statement. 

**SOQL Samples:**
```
"SELECT Id, Email FROM Contact WHERE LastName = 'Jones'"
```

As you can imagine this most likely means that you will have to have access to a Salesforce account.
Furthermore, the overall **`SELECT`** statements can vary due to the customization organizations can achieve within Salesforce. 

## Directory Structure
The overall directory is consistent with the Tab Menu Items one would normally see within the SalesForce Service Console App or the Lightning App. This directory focuses on default objects and features readily available within SalesForce. Each Menu and Options are discussed in the subsequent sections following the overall discussion around the directory structure. 

**Getting Started** 
You need to create two files within each sub-directory in order to work with the scripts. 

- A **`secrets.json`** File
```
{
  "user": {
    "username": "INSERT_USERNAME",
    "password": "INSERT_PASSWORD",
    "salesforce_token": "INSERT_TOKEN"
  }
}
```

- A **`reports.json`** File 
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
The scripts are written in such a way that information is loaded from a **`JSON`** file that is specifically set to be ignored within the repository. This means the script only pass of information if you have access to the Salesforce Organization. The ignore is set within **`.gitignore`** file at the root directory of the repository. 

## Cases
Salesforce Cases are available in both Salesforce Classic and Lightning Experience. 
A normal case view might look like the following:

![Image](https://res.cloudinary.com/hy4kyit2a/f_auto,fl_lossy,q_70/learn/modules/service_basics/service_basics_intro/images/187ead0bf0768bd9b400f7442fbe47bb_service_console_customize_plan_agents_example.png)

However, a Salesforce Classic Case view might look something similar to this:

![Image](https://www.coveo.com/-/media/library/images/feature/hero-banner/solutions/coveo-for-salesforce/besttech---insight-panel_v2-2.ashx)

## Custom
The **Custom** tab menu item contains custom Tab Menu Item options specific to your organization. 
As a result, I have set everything in here to be ignored. Allowing you to centralize python interactions in within this directory. 
There are a few scripts in this directory that will list out the objects and available custom options your organization may have available. 

## Leads 
This is the main interaction for Sales people to gain and build leads as well as follow up with people. 
It may be important to gather a quick report on your leads from within the CLI to integrate better with other platforms that are now already integrated with Salesforce. 

An Example View might look like this:
![Image](https://docs.manywho.com/wp-content/uploads/2016/10/Screen-Shot-2017-01-14-at-12.16.30-PM-minishadow.png)

## Reports
This is the main emphasis here that opens up the reports and main point of Salesforce. 
Here you can manage reports, view reports, create reports, and clone reports. Reports will vary from organizations, so I have focused on making the repository simple to delete, view, create, and clone reports. 

## Installing Requirements
To install the requirements you can simply use the following command to install all of the python requirements on your system.

- **`pip install -r requirements.txt`**

This assumes that you have **Python** installed on your machine. 
If **Python** is not installed on your machine, run over to [~/SalesforceCLI/Installation/](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Installation) and run the scripts respective to your operating system `install.sh` for Linux and/or Mac and `install.ps1` for Windows. 

## Working with SalesforceCLI as a CLI Tool 
Since the overall purpose here was to mimic an API Tool for Salesforce the main script that allows you to interact with all of the modules within this directory is the **`api_cli.py`** script. Documentation on how to use this as an API can be found on the home page of this repository. 

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
