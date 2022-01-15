import os
import uuid
from datetime import datetime

from sqlalchemy import create_engine, Table, Column, DateTime, String, Integer, MetaData, select
from sqlalchemy_utils import database_exists, create_database

def start():
    # Check if needed environmental variables exists
    necessary_env = {"database_name", "database_user", "database_pass"}
    diff = necessary_env.difference(os.environ)
    if diff:
        raise EnvironmentError(f'Please create the following environmental variables: \n{diff}')

def connect_database(table: str, user: str, password: str):
    url = f'postgresql+psycopg2://{user}:{password}@sql:5432/{table}'
    # Set echo to true to enable verbose mode. Set to false to disable
    engine = create_engine(url, echo=True)

    # check if database exists before attempting database creation.
    if not database_exists(url):
        create_database(engine.url)

    return engine

start()

# Fetch environmental variables
table_name = os.getenv("database_name", "cowry")
db_user = os.getenv("database_user", "postgres")
db_pass = os.getenv("database_pass", "postgres")
    
db_engine = connect_database(table_name, db_user, db_pass)
connection = db_engine.connect()

def create_table(engine):
    meta_data = MetaData()
    
    data_struct = Table(
        'data', meta_data,
        Column('id', Integer, primary_key=True),
        Column('created', DateTime),
        Column('uuid', String)
    )

    meta_data.create_all(engine)
    return data_struct

def add_data(to_table):
    # create data to insert into table
    to_insert = to_table.insert().values(created=datetime.now(), uuid=uuid.uuid4())
    connection.execute(to_insert)


def fetch_format_data(from_table) -> dict:
    # Fetch all data from db as well as format said data before returning
    selection = select(from_table)
    response = connection.execute(selection)
    all_data = {}

    for row in reversed(list(response)):
        all_data[str(row[1])] = row[2]

    return all_data
