# 🚀 Spark ETL DAG with Airflow, Docker & Kubernetes

This repository contains a production-ready **Apache Airflow DAG** to run Spark-based ETL workloads inside a **Kubernetes cluster** using containerized Spark jobs.

---

## 🗂️ Repository Structure

```
.
├── dags/
│   └── spark_etl_dag.py    # Airflow DAG using SparkSubmitOperator
├── Dockerfile              # Docker image for Spark ETL job runtime
└── requirements.txt        # Python dependencies
```

---

## 🧠 Purpose

This project is part of a larger **DevOps Data Engineering** workflow where:

- ETL jobs are written in **PySpark** (ETL scripts are inside the Docker image)
- Jobs are containerized using the provided `Dockerfile`
- An Airflow DAG triggers Spark jobs using **SparkSubmitOperator** on **Kubernetes**

---

## 🧱 Components

### 1️⃣ Dockerfile

- Based on `bitnami/spark`
- Copies Spark ETL scripts into `/opt/spark/app/`
- Installs Python libraries via `requirements.txt`

**Build & Push:**
```bash
docker build -t yourdockerhubuser/spark-etl:latest .
docker push yourdockerhubuser/spark-etl:latest
```

### 2️⃣ Airflow DAG (`dags/spark_etl_dag.py`)

- Triggers `extract.py`, `transform.py`, and `load.py` Spark jobs
- Uses Kubernetes configs: `spark.kubernetes.*`
- Pulls the Docker image with ETL code from a container registry

---

## 🔧 Assumptions & Requirements

- Spark ETL scripts (`extract.py`, `transform.py`, `load.py`) are baked into the Docker image
- Airflow is deployed with access to a Kubernetes cluster
- `spark_default` Airflow connection is configured properly
- Docker image is pushed to a registry accessible from Kubernetes

---

## 📦 Extended Workflow: DevOps Data Engineering Blueprint

1. **Infrastructure as Code (IaC):**
   - Use Terraform, Pulumi, or Helm to provision:
     - Cloud Storage (S3, GCS)
     - Data Warehouses (Redshift, BigQuery, Snowflake)
     - Kubernetes Clusters (EKS, GKE, AKS)
     - Airflow Deployment (Helm, MWAA, Composer)
     - CI/CD Tools (GitHub Actions, Jenkins, ArgoCD)

2. **Modular ETL Development:**
   - Write ETL logic in modular scripts: `extract.py`, `transform.py`, `load.py`
   - Keep logic decoupled from orchestration (DAG)
   - Follow repo structure: `src/`, `dags/`, `docker/`, `tests/`

3. **Author Airflow DAGs:**
   - Use `SparkSubmitOperator`, `KubernetesPodOperator`, `PythonOperator`
   - Define task dependencies, retries, timeouts
   - Make DAGs config-driven (use variables or JSON config)

4. **CI/CD Pipeline:**
   - Lint code (`flake8`, `yamllint`)
   - Run unit tests (`pytest`)
   - Validate DAGs (`airflow dags list`)
   - Build & push Docker images

5. **Image Registry Integration:**
   - Push Docker image to:
     - DockerHub
     - Amazon ECR
     - Google GCR
     - Azure ACR

6. **Run Jobs:**
   - Option A: Airflow DAG (via SparkSubmitOperator on Kubernetes)
   - Option B: Kubernetes CronJob (external to Airflow, via ArgoCD)

7. **Monitoring:**
   - Airflow UI (logs, DAG runs)
   - Prometheus + Grafana (for Spark + K8s metrics)
   - Cloud-native tools (e.g., AWS
