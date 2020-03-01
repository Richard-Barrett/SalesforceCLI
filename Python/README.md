## Python
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
- A **`reports.json`** File 

The scripts are written in such a way that information is loaded from a **`JSON`** file that is specifically set to be ignored within the repository. This means the script only pass of information if you have access to the Salesforce Organization. The ignore is set within **`.gitignore`** file at the root directory of the repository. 

## Cases

## Custom

## Leads 

## Reports
