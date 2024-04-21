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

---

## How to run this project

First of all here is the requierements

¡ This project was build with a virtual machine, especiifically Ubuntu. Data visualization wokrs with PowerBi because the port of the Postgres was configurated to be open for remote conecctions !

Install Python : [Python Downloads](https://www.python.org/downloads/)  
Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)  

This tool should be installed on windows   
Install PowerBI : [PowerBi](https://powerbi.microsoft.com/en-us/downloads/)

Steps in VM  

1. Clone this repository:
```bash
   git clone https://github.com/ManuelaMayorga/Workshop-2.git
 ```

2. Go to the project directory  
```bash
   cd Workshop-2
```

3. Create a virtual enviroment  
```bash
  python3 -m venv venv
```

4. Start the virtual enviroment  
  ```bash  
  source venv/bin/activate
  ```

5. Create into src/database a json file named `db_settings.json` and add the following keys to the file:  
```json
   {
    "user": "Your PostgreSQL database username."
    "password": "Your PostgreSQL database password."
    "host": "The host address or IP where your PostgreSQL database is running."
    "port": "The port on which PostgreSQL is listening."
    "database": "The name of your PostgreSQL database."
   }
```

6. Install necesary libreries:  
```bash
  pip install -r requirements.txt
```

7. Create a `.env` file and add this variable:  
   WORK_PATH <- Sets the working directory for the application, indicating the base path for performing operations and managing files.

8. Create a database in PostgreSQL (Make sure is the same name as your 'database' name in the json file)

9. Start with the notebooks:
- 001_load_dataGrammys.ipynb
- 002_EDA Grammys.ipynb
- 003_EDA Spotify.ipynb

10. Now for start airflow:
    
    - Export to airflow your current path
      ```bash
      export AIRFLOW_HOME=${pwd}
      ```
    - Start apache airflow
      ```bash
      airflow standalone
      ```
    - Then go to your browser a search 'localhost:8080'
   
    - And run the dag

If you have all the files and credentials fine, the dag must be working good
![Imagen de WhatsApp 2024-04-21 a las 14 36 59_c4ecaf5f](https://github.com/ManuelaMayorga/Workshop-2/assets/111150858/c7ded123-0497-4e4b-ac86-062a26b38643)

11. Once the dag has finished, Postgres should have 2 new tables and then you can go to PowerBi on Windows

12. In the terminal, run this command to see your ip and be sure to save it:
```bash
ifconfig
```   

13. Go to powerBi and follow this steps:  
    Step 1: Launch Power BI Desktop.  
    ![image](https://github.com/ManuelaMayorga/ETL_Workshop_01/assets/111150858/b25c1326-92b3-4e16-9d67-986440b1d305)

    Step 2: In the dialogue box, under the database option, select ‘PostgreSQL database’ and click ‘Connect.’  
    ![image](https://github.com/ManuelaMayorga/ETL_Workshop_01/assets/111150858/06c29b36-a1bd-47ce-8db6-1650c94fc21c)

    Step 3: In the following dialogue box, enter the server IP address and database name. (The IP address is the result of the point #12)
    ![image](https://github.com/ManuelaMayorga/ETL_Workshop_01/assets/111150858/16637fec-c01b-4580-8971-309e1ae04a93)

    Step 4: Enter your username and password in the following dialogue box and click Connect.  
    ![image](https://github.com/ManuelaMayorga/ETL_Workshop_01/assets/111150858/9631db07-0baa-4220-9af8-0242dca0a782)

    Step 5: In the navigator window, select the data that you require

**You can see my dashboard [here]()**

## Thank you for visiting this repository, remember to rate if it was helpful ⭐🐮

