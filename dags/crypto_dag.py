from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pipeline import extract_data, transform_data, load_data

def run_etl():
    data = extract_data()
    df = transform_data(data)
    load_data(df)

with DAG(
    dag_id="crypto_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_etl
    )