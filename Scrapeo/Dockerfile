FROM apache/airflow:2.2.4-python3.9
COPY requirements.txt /requirements.txt
USER root
RUN apt-get update 
RUN apt-get install -y git
USER 50000
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt


