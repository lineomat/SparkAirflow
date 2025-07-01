## Apache Airflow on Steroids with Java, Scala and Python Spark Jobs

##### This project orchestrates Spark jobs written in different programming languages using Apache Airflow, all within a Dockerized environment. The DAG sparking_flow is designed to submit Spark jobs written in Python, Scala, and Java, ensuring that data processing is handled efficiently and reliably on a daily schedule.

### Project Structure

The DAG _SparkAirflow_ includes the following tasks:

_start_: A PythonOperator that prints "Jobs started".
_python_job_: A SparkSubmitOperator that submits a Python Spark job.
_scala_job_: A SparkSubmitOperator that submits a Scala Spark job.
_java_job_: A SparkSubmitOperator that submits a Java Spark job.
_end_: A PythonOperator that prints "Jobs completed successfully".
These tasks are executed in a sequence where the _start_ task triggers the Spark jobs in parallel, and upon their completion, the _end_ task is executed.

### Prerequisites:
Before setting up the project, ensure you have the following:
+ Docker and Docker Compose installed on your system.
+ Apache Airflow Docker image or a custom image with Airflow installed.
+ Apache Spark Docker image or a custom image with Spark installed and configured to work with Airflow.
+ Docker volumes for Airflow DAGs, logs, and Spark jobs are properly set up.

### Docker Setup:
To run this project using Docker, follow these steps:

  1. Clone this repository to your local machine.
  2. Navigate to the directory containing the _docker-compose.yml_ file.
  3. Build and run the containers using Docker Compose:
      _docker-compose up -d --build_
