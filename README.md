# DataOps-Project
# Spark ETL Pipeline on Airflow & Kubernetes

This repo contains a data engineering pipeline built with Spark, scheduled by Airflow, and deployed in Kubernetes.

## Structure
- `spark_jobs/`: Python scripts for Extract, Transform, Load
- `dags/`: Airflow DAG using SparkSubmitOperator
- `Dockerfile`: Builds a Spark-ready container with ETL code
- `requirements.txt`: Python dependencies for Spark jobs

## Usage
1. Build & push Docker image
2. Deploy Airflow with KubernetesExecutor
3. Add DAG to Airflow
4. Ensure Spark image is pullable by your cluster


