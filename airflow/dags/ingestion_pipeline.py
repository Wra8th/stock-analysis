from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import requests
import yfinance as yf
from datetime import date
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

current_date = date.today()
ticker = 'GME'


def fetch_data():
    data = yf.download([ticker, "INTC"], period='1y', interval='1d')
    data.to_csv(f'/opt/airflow/data/raw/{ticker}-INTC-{current_date}-data.csv')

def upload_to_s3():
    local_file_path = f'/opt/airflow/data/raw/{ticker}-INTC-{current_date}-data.csv'  # path inside container
    bucket_name = "stock-data-rawingested"
    s3_key = f'{ticker}-INTC-{current_date}-data.csv' # S3 path

    hook = S3Hook(aws_conn_id="aws-s3-stock")  # Or set to None if using env vars
    hook.load_file(
        filename=local_file_path,
        key=s3_key,
        bucket_name=bucket_name,
        replace=True
    )

dag = DAG(
    'ingestion-pipeline',
    default_args={'start_date': days_ago(1)},
    schedule_interval='0 23 * * *',
    catchup=False
)

fetch_data_task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    dag=dag
)

upload_task = PythonOperator(
    task_id="upload_to_s3",
    python_callable=upload_to_s3
)

# Set the dependencies between the tasks
fetch_data_task >> upload_task