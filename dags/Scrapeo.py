# Imports del Script
import time
import os

# Cosas de Airflow
from datetime import datetime, timedelta
from airflow.models import dag
from airflow.operators.bash import BashOperator
import airflow

args={
    'owner': 'Tomás',
}

dt = datetime.strptime('19 Aug 2021', '%d %b %Y')
newdatetime = dt.replace(hour=14, minute=50)

dag = dag.DAG(
    default_args=args,
    dag_id='Scrapeo',
    start_date= airflow.utils.dates.days_ago(2),
    schedule_interval=('0 3 * * *'),
    description='Scrapeo de los datos y creación de las imágenes',
    tags=['Scrapping'],
    catchup=False)

with dag:

    Scrapeo = BashOperator(
        task_id='Scrapping',
       bash_command='python /opt/airflow/Scripts/Scrapper.py',
    )

    

    Scrapeo