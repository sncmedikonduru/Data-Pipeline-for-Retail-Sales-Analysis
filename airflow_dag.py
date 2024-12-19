from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.ingest import ingest_data
from scripts.clean import clean_data
from scripts.feature_engineering import feature_engineering
from scripts.analyze import analyze_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'retail_sales_analysis_pipeline',
    default_args=default_args,
    description='A data pipeline for retail sales analysis',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 12, 1),
    catchup=False,
) as dag:

    ingest_task = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data,
        op_kwargs={'file_path': 'data/sales_data.csv'},
    )

    clean_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
        op_kwargs={'data': "{{ ti.xcom_pull(task_ids='ingest_data') }}"},
    )

    feature_engineering_task = PythonOperator(
        task_id='feature_engineering',
        python_callable=feature_engineering,
        op_kwargs={'data': "{{ ti.xcom_pull(task_ids='clean_data') }}"},
    )

    analyze_task = PythonOperator(
        task_id='analyze_data',
        python_callable=analyze_data,
        op_kwargs={'data': "{{ ti.xcom_pull(task_ids='feature_engineering') }}"},
    )

    ingest_task >> clean_task >> feature_engineering_task >> analyze_task
