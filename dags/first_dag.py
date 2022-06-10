from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from textwrap import dedent

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


def get_first_task():
    print(f"This is my first DAG")


def get_second_task():
    print(f"This is my first DAG - second task")


with DAG(
    'first_dag',
    default_args=default_args,
    description='Our first DAG',
    schedule_interval=timedelta(days=1),
    tags=['first_DAG']
) as dag:

    task_1 = PythonOperator(
        task_id='first_task',
        python_callable=get_first_task,
        dag=dag
    )

    task_1.doc_md = dedent(
        """\
#### Task Documentation
You can document your task using the attributes `doc_md` (markdown),
`doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
rendered in the UI's Task Instance Details page.
![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)

"""
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG
    dag.doc_md = """
    This is some custom documentation .... :))))))
    """

    task_2 = PythonOperator(
        task_id='second_task',
        python_callable=get_second_task,
        dag=dag
    )

    task_1 >> task_2
