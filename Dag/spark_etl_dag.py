from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='spark_etl_pipeline',
    description='ETL pipeline using Spark on Kubernetes',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['spark', 'etl'],
) as dag:

    extract = SparkSubmitOperator(
        task_id='extract_data',
        application='local:///opt/spark/app/extract.py',
        conn_id='spark_default',
        conf={
            'spark.master': 'k8s://https://kubernetes.default.svc',
            'spark.kubernetes.container.image': 'yourdockerhubuser/spark-etl:latest',
            'spark.kubernetes.namespace': 'your-k8s-namespace',
            'spark.executor.instances': '2',
        },
        deploy_mode='cluster'
    )

    transform = SparkSubmitOperator(
        task_id='transform_data',
        application='local:///opt/spark/app/transform.py',
        conn_id='spark_default',
        conf={
            'spark.master': 'k8s://https://kubernetes.default.svc',
            'spark.kubernetes.container.image': 'yourdockerhubuser/spark-etl:latest',
            'spark.kubernetes.namespace': 'your-k8s-namespace',
            'spark.executor.instances': '2',
        },
        deploy_mode='cluster'
    )

    load = SparkSubmitOperator(
        task_id='load_data',
        application='local:///opt/spark/app/load.py',
        conn_id='spark_default',
        conf={
            'spark.master': 'k8s://https://kubernetes.default.svc',
            'spark.kubernetes.container.image': 'yourdockerhubuser/spark-etl:latest',
            'spark.kubernetes.namespace': 'your-k8s-namespace',
            'spark.executor.instances': '2',
        },
        deploy_mode='cluster'
    )

    # Set task dependencies
    extract >> transform >> load