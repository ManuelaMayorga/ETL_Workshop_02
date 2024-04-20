from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.decorators import dag, task
import os
import sys
sys.path.append(os.path.abspath("/home/manuela/prueba/dags/etl_dag_folder"))

from etl import *


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 12),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

@dag(
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval='@daily',
)
def etl_dag():

    @task
    def db_connect():
        return grammy_process()
    
    @task
    def transform_db(json_data):
        return transform_grammys_data(json_data)
    
    @task
    def read_csv_task():
        return read_csv_spotify()
    
    @task
    def spotify_trasnformation(json_data):
        return transform_spotify_data(json_data)

    @task
    def merge_data(json_df1, json_df2):
        return merge(json_df1, json_df2)
    
    @task
    def load(json_data):
        return load_merge(json_data)
    
    @task
    def store(json_data):
        return subir_archivo(json_data, 'data_music.csv', '13KAmiIkiZe7Rb0YDuE_vI0gkfERbICmn') 

    grammys_read = db_connect()
    transformation_grammys = transform_db(grammys_read)
    
    spotify_read = read_csv_task() 
    transformation_spotify = spotify_trasnformation(spotify_read) 

    data_merge = merge_data(transformation_grammys, transformation_spotify)

    load_data = load(data_merge)

    store_data = store(load_data)

workflow_api_etl_dag = etl_dag()

