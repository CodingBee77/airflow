# airflow

Set of basic scripts that runs DAG written in Python using Apache Airflow.

![This is an image](airflow_img.png)

## Configuration and installation

Airflow runs in a docker container, docker-compose file can be fetched from the remote repository running the command:
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.2/docker-compose.yaml'
```

'docker-compose.yaml' contains several services such as:

- airflow-scheduler - The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.

-airflow-webserver - The webserver is available at http://localhost:8080.

- airflow-worker - The worker that executes the tasks given by the scheduler.

- airflow-init - The initialization service.

- postgres - The database.

- redis - The redis - broker that forwards messages from scheduler to worker.

More details about airflow and its configuration in a docker container can be found under link below:
[Running Airflow in Docker ](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)


Repository contains following scripts:
- first_dag.py : create a workflow consists of 2 tasks, using PythonOperator
- second_dag.py: create a workflow of 3 tasks that uses BashOperator
- dag_with_parameters.py : runs 1 task with function that takes 2 arguments 
- dag_xcom.py : uses XCom  (short for "cross-communications") to pull/push information and enable
communication between tasks



Important links:
https://airflow.apache.org/
