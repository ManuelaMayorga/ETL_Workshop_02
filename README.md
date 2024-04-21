# Workshop_02 - ETL process using airflow
Autor: [@ManuelaMayorga](https://github.com/ManuelaMayorga)

---
## Welcome

This project is an exercise on how to build an ETL pipeline using Apache Airflow, the idea is to extract information using three different data sources (csv file and database), then do some transformations and merge the transformed data to finally load into google drive as a CSV file and store the data in a DB. As a last step, create a data visualizations.
Throughout this process, specific technologies were used including:

- _Python_ <img src="https://cdn-icons-png.flaticon.com/128/3098/3098090.png" alt="Python" width="21px" height="21px"> 
- _Jupyter Notebook_  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" alt="Jupyer" width="21px" height="21px">
- _PostgreSQL_ as the relational database management system (this was chosen by personal preference). <img src="https://cdn-icons-png.flaticon.com/128/5968/5968342.png" alt="Postgres" width="21px" height="21px">
- _Apache Airflow_  <img src="https://miro.medium.com/v2/resize:fit:1358/0*sesfl3V6mvwVQUb1" width="21px" height="21px">

---

## Objectives  

1. Use Apache Airflow to read data from multiple sources, such as CSV files and databases.
2. Apply transformations to the data read using Apache Airflow.
3. upload the transformed data to an external storage platform (Google Drive)
4. Merge data sets
5. Use PowerBI to visualize information

---
## Workflow

![Workflow_Manuela](https://github.com/ManuelaMayorga/Workshop-2/assets/111150858/6f4eee9b-e2b5-4d1a-93cb-9d89d39ce29b)

---

## Data Source

These are the datasets used in this project, additionally we specify which one is going to be read from python and which one is going to be read from the database  

- Dataset to be readed as CSV: [Spotify dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)  

- Dataset to be loaded into the initial database: [Grammys Dataset](https://www.kaggle.com/datasets/unanimad/grammy-awards)

---

## Folders path

![tree_manuela](https://github.com/ManuelaMayorga/Workshop-2/assets/111150858/1b3d485b-aa3b-4f6c-96a0-039137769db6)




