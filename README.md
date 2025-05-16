# ETL-using-Airflow-and-BashOperator
Analyzed road traffic data from multiple toll plazas across different highways, each managed by distinct toll operators using varied IT systems and file formats. Consolidated heterogeneous data sources into a unified, standardized file for streamlined analysis and reporting.
This project is completed on Coursera’s cloud environment

## Tools Used: Apache Airflow, Python, Kafka


##	Extract data from a csv file
![extract_Data_from_csv](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/extract_data_from_csv.png)
##	Extract data from a tsv file
![extract Data from tsv](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/extract_data_from_tsv.png)

##	Extract data from a fixed-width file
![Extract_data from fixed width file](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/extract_data_from_fixed_width.png)
##	Transform the data
![transform_Data](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/transform.png)

## Load the transformed combined data
![Load Transformed combined data](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/consolidate_data.png)

##	After python script is done, save it.
[Link to ETL project python script](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/ETL_toll_data_bash_operator.py)
##	Submit a DAG
* Export AIRFLOW_HOME=/home/project/airflow
* 	Cp ETL_toll_data.py $AIRFLOW_HOME/dags

##	Verify if DAG is submitted or not
![Submit DAG](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/submit_dag.png)

##	If can not find DAG then run below command to check errors, resolve error delete python file from dag folder and again copy using above cp command.
*	Airflow dags list-import-errors

## Airflow UI 
![audit_log_airflow](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/audit_log_airflow.png)
![Dag is running](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/dag_runs.png)
![dag tasks graph view](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/dag_tasks.png)
![Details tab of DAG](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/details.png)
![run duration option](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/run_duration_option.png)

## Kafka real time data pipeline : road traffic data from national hiway toll plaza, as vehical pass through key data- vehical id, type, toll plaza id and timestamp is streamed via kafka.
[Kafka real time data](https://github.com/Dipapatil/ETL-using-Airflow-and-BashOperator/blob/main/Streaming%20ETL%20Pipeline%20using%20Kafka%20project.docx)

