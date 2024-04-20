import sys
import os

sys.path.append(os.path.abspath("/home/manuela/prueba"))

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

from transformation.grammys import *
from transformation.spotify import *
from src.database.connection import config_loader
from sqlalchemy.orm import sessionmaker
from src.data_process.class_processor import Processor	
from sqlalchemy import inspect, Table, MetaData, insert, select
from src.models.models import Grammys
from src.models.models import DataMusic
import logging
import json

logging.basicConfig(level=logging.INFO)


#### DATA GRAMMYS

def grammy_process():
    """
    Function to process Grammy data, including table creation, data insertion, and retrieval.

    Returns:
    str: JSON string representing the processed data.
    """

    connection = config_loader()
    Session = sessionmaker(bind=connection)
    session = Session()

    try:
        try:
            if inspect(connection).has_table('grammys'):
                Grammys.__table__.drop(connection)
                logging.info("Table dropped successfully.")
                Grammys.__table__.create(connection)
                logging.info("Table created successfully.")
                
            else:
                Grammys.__table__.create(connection)
                logging.info("Table created successfully.")

        except Exception as e:
            logging.error(f"Error creating table: {e}")

        data = Processor('data/the_grammy_awards.csv')
        data.insert_id()
        df = data.df

        try:
            metadata = MetaData()
            table = Table('grammys', metadata, autoload=True, autoload_with=connection)

            with connection.connect() as conn:
                values = [{col: row[col] for col in df.columns} for _, row in df.iterrows()]

                conn.execute(insert(table), values)
            
            logging.info("Data inserted successfully.")
        except Exception as e:
            logging.error(f"Error inserting data: {e}")
        
        select_stmt = select([table])
        result_proxy = connection.execute(select_stmt)
        results = result_proxy.fetchall()
        column_names = table.columns.keys()
        df_2 = pd.DataFrame(results, columns=column_names)

        logging.info("Data loaded successfully.")

        return df_2.to_json(orient='records')

    except Exception as e:
        logging.error(f"Error processing data: {e}")


def transform_grammys_data(json_data):
    """
    Transforms Grammy data by processing, cleaning, and restructuring it.

    Args:
    json_data (str): JSON string containing Grammy data.

    Returns:
    str: JSON string representing the transformed data.
    """

    json_data = json.loads(json_data)
    df = pd.DataFrame(json_data)

    df = process_data(df)
    df = drop_rows(df)
    df = clean_artist(df)
    df = rename_column(df)
    df = drop_columns(df)
    
    logging.info('Data transformed successfully')
    return df.to_json(orient='records')


#### DATA SPOTIFY

def read_csv_spotify():
    """
    Reads Spotify dataset from a CSV file and converts it to JSON format.

    Returns:
    str: JSON string representing the Spotify dataset.
    """
    df = pd.read_csv('data/spotify_dataset.csv')
    logging.info('Data loaded successfully')
    return df.to_json(orient='records')


def transform_spotify_data(json_data):
    """
    Transforms Spotify data by cleaning, categorizing, and processing it.

    Args:
    json_data (str): JSON string containing Spotify data.

    Returns:
    str: JSON string representing the transformed data.
    """
    logging.info('Data coming from: ', json_data)

    json_data = json.loads(json_data)
    df = pd.DataFrame(json_data)

    df = drop_columns_spotify(df)
    df = drop_track_id(df)
    df = drop_duplicate_rows(df)
    df = assign_popularity_levels(df)
    df = convert_duration(df)
    df = categorize_danceability(df)
    df = categorize_speechiness(df)
    df = assign_valence_categories(df)
    df = assign_genre_categories(df)
    df = drop_columns_unnecessary(df)

    logging.info('Data transformed successfully')
    return df.to_json(orient='records')


#### MERGE

def merge(json_df1, json_df2):
    """
    Merges two JSON datasets based on specific columns, fills null values, and performs additional data processing.

    Args:
    json_df1 (str): JSON string containing the grammys dataset.
    json_df2 (str): JSON string containing the spotify dataset.

    Returns:
    str: JSON string representing the merged dataset.
    """

    df1 = pd.DataFrame(json.loads(json_df1))
    df2 = pd.DataFrame(json.loads(json_df2))

    df_merged = df2.merge(df1, how='left', left_on='track_name', right_on='nominee')
    
    columns1 = ['year']
    fill_null_values(df_merged, columns1, 0)

    columns2 = ['category', 'nominee', 'artist']
    fill_null_values(df_merged, columns2, 'Not nominated')

    columns3 = ['nominated']
    fill_null_values(df_merged, columns3, 0)

    columns4 = ['nominated']
    replace_true_values(df_merged, columns4, 1)

    column_year(df_merged, 'year')

    logging.info(df_merged.head(3))
    logging.info(df_merged.isnull().sum())    
    logging.info('Data merged successfully')
    return df_merged.to_json(orient='records')

    
def load_merge(json_data):
    """
    Loads JSON data into a DataFrame, performs a merge operation, and inserts the merged data into a database table.

    Args:
    json_data (str): JSON string containing the data to be loaded and merged.

    Returns:
    str: JSON string representing the merged data.
    """
    json_data = json.loads(json_data)
    df = pd.DataFrame(json_data)

    df.insert(0, 'id', df.index + 1)

    connection = config_loader()

    try:
        if inspect(connection).has_table('data_music'):
            DataMusic.__table__.drop(connection)
            logging.info("Table dropped successfully.")
        
        DataMusic.__table__.create(connection)
        logging.info("Table created successfully.")

        metadata = MetaData()
        table = Table('data_music', metadata, autoload=True, autoload_with=connection)

        with connection.connect() as conn:
            values = [{col: row[col] for col in df.columns} for _, row in df.iterrows()]

            conn.execute(insert(table), values)

        logging.info('Data loaded successfully')

        return df.to_json(orient='records')
    
    except Exception as e:
        logging.error(f"Error processing data: {e}")


directorio_credentiales = 'credentials_module.json'

### START OF PYDRIVE AUTHENTICATION

def login():
    """
    Authenticates with Google Drive using PyDrive.

    Returns:
    GoogleDrive: GoogleDrive instance for accessing Drive API.
    """
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credentiales)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(directorio_credentiales)
    else:
        gauth.Authorize()
    
    return GoogleDrive(gauth)


def file_upload(json_data, file_title, id_folder):
    """
    Uploads a CSV file to the specified directory in Google Drive.

    Args:
    json_data (str): JSON string containing the data to be converted to CSV and uploaded to the file.
    file_title (str): Title of the file to be uploaded.
    id_folder (str): ID of the Google Drive directory where the file will be uploaded.

    Returns:
    None
    """
    json_data = json.loads(json_data)
    df = pd.DataFrame(json_data)

    df_to_csv = df.to_csv(index=False) 

    credenciales = login()

    file = credenciales.CreateFile({'title' : file_title ,
                             'parents': [{'kind': 'drive#fileLink', 'id': id_folder}],
                             'mimeTypp': 'text/csv'})
    
    file.SetContentString(df_to_csv) 
    file.Upload()

### References PyDrive
# MoonCode. (2021, 7 marzo). Aprende a usar Google Drive con Python en 20 minutos 😃💻-Learn Python and Google Drive in 20 minutes [Vídeo]. YouTube. https://www.youtube.com/watch?v=ZI4XjwbpEwU 
# Welcome to PyDrive’s documentation! — PyDrive 1.2.1 documentation. (s. f.). https://pythonhosted.org/PyDrive/ 