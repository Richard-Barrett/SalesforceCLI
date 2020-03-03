# SalesforceCLI
A CLI Tool for Working with Your Organizations SFDC

![Image](https://triking-creative.s3.amazonaws.com/Logos/SalesforceCLI/SalesfroceCLI_A.jpg)

## Directory Structure
The overall structure is split into overall interaction within a SalesForce Organization. 
- **[Documentation](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Documentation)**: contains any and all documentation related to the repository including a man page. 
- **[Installation](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Installation)**: contains installation scripts for the overall repository.
- **[Integration](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Integration)**: contains integration plugins for the repository.
- **[Lightning](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Integration)**: contains Lightning scripts to interact with Lightning expeirence.
- **[Plotly](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Plotly)**: contains visualization scripts to visualize overall data structures within a Plotly Instance.
- **[Python](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Python)**: contains overall python scripts that allow for interaction within the terminal as a CLI tool.
- **[Queries](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Queries)**: contains a query builder script, as well as query modules that allow you to customize your own queries.
- **[Reporting](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Reporting)**: contains interactions to scrape information from the Reporting feature within Salesforce
- **[Samples](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/Samples)**: contains samples from **`SOQL`** scripts to overall python scripts. 
- **[ServiceConsole](https://github.com/Richard-Barrett/SalesforceCLI/tree/master/ServiceConsole)**: contains overall interactions allowed to users with service console application access within a SalesForce Organization

## Commands
Main Syntax 
```
sfdc <Argument> --Flag Flag-String Options=Value
```

Example to pull out a report on Sev2 Cases:
```
sfdc cases --report sev2 time-frame=today
```

## Arguments
```
cases

custom

leads

reports
```
## Flags
```
-r, --report 
```
## Options
```
time-frame
severity-level
```
