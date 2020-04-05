from pandas import DataFrame
from simple_salesforce import SalesforceAPI

sf = SalesforceAPI('<insert_username>', '<insert_password>', '<insert_token>')

# Saleforce Secure Connection TBD
# ===============================
# sf_sec = Salesforce(username = username,
#               password = password,
#               security_token= token,
#               instance_url = instance,
#               sandbox = isSandbox)

# Function to Return Salesforce SOQL Queries as Dataframes
# =========================================================
def sql_query(query_str):
    qry_result = sf.query(query_str)
    print('Record Count {0}'.format(qry_result['totalSize']))
    is_done = qry_result['done']
    if is_done:
        df = DataFrame(qry_result['records'])
    while not is_done:
        try:
            if not qry_result['done']:
                df = df.append(DataFrame(qry_result['records']))
                qry_result = sf.query_more(qry_result['nextRecordsUrl'], True)
            else:
                df = df.append(DataFrame(qry_result['records']))
                is_done = True
                print('completed')
                break
        except NameError:
            df = DataFrame(qry_result['records'])
            sf.query_more(qry_result['nextRecordsUrl'], True)
    df = df.drop('attributes', axis=1)
    return df

#   SAMPLE SOQL COMMANDS
# ===========================
# SOQL('SELECT Id FROM CASE')
soql_test = 'SELECT Milestone_violated__c, First_Reply__c, CaseNumber, Environment2__r.Name,' \
            ' Owner.Name, Severity_Level__c, Status, Subject, URL_for_support__c from Case'
            
res = sql_query(soql_test)
print(res)
