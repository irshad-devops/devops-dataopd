from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG('flight_data_pipeline_final', start_date=datetime(2026, 1, 1), schedule='@daily', catchup=False) as dag:

    # Quality Gate
    validate = BashOperator(
        task_id='validate_data_quality',
        bash_command='python3 /opt/airflow/scripts/validate_flights.py'
    )

    # Security & Transformation
    secure_data = BashOperator(
        task_id='secure_and_mask_pii',
        bash_command='spark-submit /opt/airflow/scripts/secure_flight_data.py'
    )

    validate >> secure_data
