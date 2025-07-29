# DataOps-Project
# Spark ETL Pipeline on Airflow & Kubernetes

This repository contains a production-ready **Apache Airflow DAG** to run Spark-based ETL workloads inside a **Kubernetes cluster** using containerized Spark jobs.

---

## 🗂️ Repository Structure

.
├── dags/
│ └── spark_etl_dag.py # Airflow DAG using SparkSubmitOperator
├── Dockerfile # Docker image for Spark ETL job runtime
└── requirements.txt # Python dependencies (if used in Spark jobs)

---

## 🧠 Purpose

This project is part of a larger DevOps Data Engineering workflow where:

- ETL jobs are written in PySpark (not included in this repo)
- Those jobs are containerized with dependencies using the provided `Dockerfile`
- Airflow DAG triggers Spark jobs via Kubernetes (`SparkSubmitOperator`)

---

## 🧱 Components Overview

### ✅ 1. Dockerfile

- Base image: `bitnami/spark`
- Copies ETL scripts (if present) to `/opt/spark/app/`
- Installs additional Python libraries from `requirements.txt` (optional)

Example build/push:

```bash
docker build -t yourdockerhubuser/spark-etl:latest .
docker push yourdockerhubuser/spark-etl:latest
✅ 2. Airflow DAG (dags/spark_etl_dag.py)
Uses SparkSubmitOperator to trigger Spark jobs:

extract.py, transform.py, load.py (assumed to be in image)

Runs Spark on Kubernetes using the spark.kubernetes.* configs

Configurable Docker image, namespace, and resources

🔧 Assumptions & Requirements
Spark jobs (extract.py, transform.py, load.py) are part of the Docker image

Airflow is running with access to a Kubernetes cluster

The spark_default Airflow connection is properly set up

Docker image is pushed to a registry accessible from K8s
