## Apache Airflow on Steroids with Java, Scala and Python Spark Jobs

##### This project orchestrates Spark jobs written in different programming languages using Apache Airflow, all within a Dockerized environment. The DAG sparking_flow is designed to submit Spark jobs written in Python, Scala, and Java, ensuring that data processing is handled efficiently and reliably on a daily schedule.

### Project Structure

The DAG ######_SparkAirflow_ includes the following tasks:

_start_: A PythonOperator that prints "Jobs started".
_python_job_: A SparkSubmitOperator that submits a Python Spark job.
_scala_job_: A SparkSubmitOperator that submits a Scala Spark job.
_java_job_: A SparkSubmitOperator that submits a Java Spark job.
_end_: A PythonOperator that prints "Jobs completed successfully".
These tasks are executed in a sequence where the start task triggers the Spark jobs in parallel, and upon their completion, the end task is executed.
