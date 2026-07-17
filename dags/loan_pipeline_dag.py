from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "guransh",
    "start_date": datetime(2025, 5, 24),
    "retries": 1,
}

with DAG(
    dag_id="loan_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
    description="Loan Risk ETL Pipeline",
) as dag:

    etl_task = BashOperator(
        task_id="etl_task",
        bash_command="cd /opt/airflow && python etl.py"
    )

    validation_task = BashOperator(
        task_id="data_validation",
        bash_command="cd /opt/airflow && python tests/data_validation.py"
    )

    business_rule_task = BashOperator(
        task_id="business_rule_tests",
        bash_command="cd /opt/airflow && python tests/business_rule_tests.py"
    )

    reconciliation_task = BashOperator(
        task_id="reconciliation_test",
        bash_command="cd /opt/airflow && python tests/reconciliation_test.py"
    )

    upload_task = BashOperator(
        task_id="upload_to_bigquery",
        bash_command="cd /opt/airflow && python upload_to_bq.py"
    )

    sql_task = BashOperator(
        task_id="run_sql_queries",
        bash_command="cd /opt/airflow && python run_queries.py"
    )

    etl_task >> validation_task >> business_rule_task >> reconciliation_task >> upload_task >> sql_task