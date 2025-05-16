from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'testing_bash_etl',
    'start_date': days_ago(0),
    'email': ['test@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='ETL toll data dag - Apache Airflow final Assingment',
    schedule_interval=timedelta(days=1),
)

# define task, here tar is used to unzip
unzip_data=BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvf /home/project/airflow/dags/finalassignment/tolldata.tgz',
    dag=dag,
)

# extract data from csv file and save it in another csv file, here cut command is used, -d shows delimiter here it is comma, f indicates field 

extract_data_from_csv=BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1,2,3,4 vehicle-data.csv > csv_data.csv',
    dag=dag,
)

# extract data from tsv file, and > is used to override the file with new data, if we use << then it will append data

extract_data_from_tsv=BashOperator(
    task_id='extract_data_from_tsv_file',
   bash_command="cut -d\$'\t' -f5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > tsv_data.csv",
    dag=dag,
)

# to extract data from fixed width file we can not use field(f), will have to use character

extract_data_from_fixed_width=BashOperator(
    task_id='extract_data_from_fixed_width_file',
    bash_command='cut -c 48-61,62-65 /home/project/airflow/dags/finalassignment/payment-data.txt > fixed_width_data.csv',
    dag=dag,
)

# using paste to combine csv files to create one
consolidate_data=BashOperator(
    task_id='consolidate_data',
    bash_command='paste csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv',
    dag=dag,
)

# transform
transform_data=BashOperator(
    task_id='transform_data_task',
    bash_command="cut -f 4 extracted_data.csv | tr '[a-z]' '[A-Z]' > transformed_data.csv",
    dag=dag,
)


unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data