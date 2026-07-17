import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "loan-risk-project-ff7bb1ae2f92.json"
)

client = bigquery.Client(
    credentials=credentials,
    project="loan-risk-project"
)

df = pd.read_csv("cleaned_loan_risk_data0001.csv")

table_id = "loan-risk-project.loan_analytics.loan_data"

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE"
)

job = client.load_table_from_dataframe(
    df,
    table_id,
    job_config=job_config
)

job.result()

print("Data uploaded successfully!")