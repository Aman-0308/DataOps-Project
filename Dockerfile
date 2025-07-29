# Use Bitnami Spark base image (includes Hadoop and Spark pre-installed)
FROM bitnami/spark:latest

# Create app directory inside the container
RUN mkdir -p /opt/spark/app

# Copy ETL scripts into container
COPY spark_jobs/*.py /opt/spark/app/

# Set working directory
WORKDIR /opt/spark/app/


# Install additional Python dependencies if needed
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3-pip && pip3 install -r requirements.txt

# Default command (optional - typically overridden by SparkSubmitOperator)
CMD ["spark-submit", "--help"]
