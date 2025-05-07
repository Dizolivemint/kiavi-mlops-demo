from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Extracting data...")

def train():
    print("Training model...")

with DAG("property_value_pipeline", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    train_task = PythonOperator(task_id="train", python_callable=train)
    extract_task >> train_task
