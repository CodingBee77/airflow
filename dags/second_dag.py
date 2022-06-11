from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Martyna',
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='second_dag_v3',
    default_args=default_args,
    description='My second DAG',
    start_date=datetime(2022, 6, 7, 12),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task !'
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hello I am task2 and will be running after task1 !'
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hey, I am task3 and will be running after task2 !'
    )

    task1.set_downstream(task2)
    task2.set_downstream(task3)
