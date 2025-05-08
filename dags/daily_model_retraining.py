
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    dag_id='daily_model_retraining',
    default_args=default_args,
    description='Retrain the model daily using updated property data',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['mlflow', 'retraining'],
) as dag:

    def run_training_script():
        subprocess.run(["python", "mlflow_multiple_runs.py"], check=True)

    retrain_task = PythonOperator(
        task_id='retrain_model',
        python_callable=run_training_script
    )

    retrain_task
