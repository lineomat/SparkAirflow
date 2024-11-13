FROM apache/airflow:2.10.2-python3.11

USER root
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-17-jdk && \
    apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
ENV PYSPARK_PYTHON python3

USER airflow

RUN pip install apache-airflow apache-airflow-providers-apache-spark pyspark
