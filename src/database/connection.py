from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import json
import os

import logging

logging.basicConfig(level=logging.INFO)

def config_loader():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'db_settings.json')

    try:
        with open(file_path) as f:
            parameters = json.load(f)

        url = f"postgresql://{parameters['user']}:{parameters['password']}@{parameters['host']}:{parameters['port']}/{parameters['database']}"
        engine = create_engine(url)
        logging.info(f'Connected successfully to {parameters["database"]} database')
        return engine

    except FileNotFoundError:
        logging.error(f'Error: File not found at path {file_path}')
        return None  
    
    except SQLAlchemyError as e:
        logging.error(f'Error: {e}')
        return None  
