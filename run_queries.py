from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "loan-risk-project-ff7bb1ae2f92.json"
)

client = bigquery.Client(
    credentials=credentials,
    project="loan-risk-project"
)
with open("sql/risk_analysis.sql","r") as file:
    query=file.read()
    query_job = client.query(query)
    results = query_job.result()
    print("Query Results:\n")
    for row in results:
        print(row)