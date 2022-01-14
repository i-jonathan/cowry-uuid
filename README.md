## Basic Requirements
- Python3
- FastAPI
- Postgres
- Uvicorn

###### All package requirements can be found in the requirements.txt file

## Environmental Variables Required
- database_user
- database_name
- database_pass

## Start
To run application, install all required packages

	$ pip install -r requirements.txt

Create postgres database with name in $database_name

Run application with

	$ unicorn main:app --reload

Visit 127.0.0.1:8000
