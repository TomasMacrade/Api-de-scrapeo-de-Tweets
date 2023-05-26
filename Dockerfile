FROM apache/airflow:2.6.1-python3.9
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
RUN pip install --upgrade pip ipython ipykernel
RUN ipython kernel install --name "python3" --user


USER root