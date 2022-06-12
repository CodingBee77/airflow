from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 6, 7),
    'retries': 2,
    'retry_delay': timedelta(minutes=10)
}


def greet(name, age):
    print(f"Hello World! My name is {name}, "
          f"and I am {age} years old. ")


with DAG(
    'dag_with_parameter_v2',
    default_args=default_args,
    description='Some DAG',
    schedule_interval=timedelta(days=1),
    tags=['param_DAG']
) as dag:

    task_1 = PythonOperator(
        task_id='first_task',
        python_callable=greet,
        op_kwargs={'name': 'Tom', 'age': 20}
    )
