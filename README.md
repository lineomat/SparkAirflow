## Apache Airflow on Steroids with Java, Scala and Python Spark Jobs

##### This project orchestrates Spark jobs written in different programming languages using Apache Airflow, all within a Dockerized environment. The DAG sparking_flow is designed to submit Spark jobs written in Python, Scala, and Java, ensuring that data processing is handled efficiently and reliably on a daily schedule.

### Project Structure

###### The DAG sparking_flow includes the following tasks:

start: A PythonOperator that prints "Jobs started".
python_job: A SparkSubmitOperator that submits a Python Spark job.
scala_job: A SparkSubmitOperator that submits a Scala Spark job.
java_job: A SparkSubmitOperator that submits a Java Spark job.
end: A PythonOperator that prints "Jobs completed successfully".
