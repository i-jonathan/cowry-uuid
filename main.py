from fastapi import FastAPI
from app import create_table, fetch_format_data, add_data, db_engine

app = FastAPI()

@app.get("/")
def home():
    # creates data table
    uuid_table = create_table(db_engine)

    # adds new uuid data to db
    add_data(uuid_table)

    # retrieve data from db and format to json
    result = fetch_format_data(uuid_table)
    return result 

