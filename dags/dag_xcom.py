from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 6, 7),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=10)
}


def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World! My name is {first_name} {last_name}, "
          f"and I am {age} years old. ")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Sarah')
    ti.xcom_push(key='last_name', value='Freedman')


def get_age(ti):
    ti.xcom_push(key='age', value=20)


with DAG(
    dag_id='dag_xcom_v4',
    default_args=default_args,
    description='DAG xcom',
    schedule_interval=timedelta(days=1),
    tags=['xcom_DAG']
) as dag:

    task_1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )

    task_2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task_3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task_2, task_3] >> task_1
