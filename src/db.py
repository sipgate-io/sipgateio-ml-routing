import mysql.connector
from mysql.connector import Error
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

host = os.environ.get("DATABASE_HOST") or 'localhost'
username = os.environ.get("DATABASE_USERNAME") or 'admin'
password = os.environ.get("DATABASE_PASSWORD") or 'admin'

mydb = mysql.connector.connect(
    host=host,
    user=username,
    password=password
)

def execute_query(query):
    cursor = mydb.cursor()
    try:
        cursor.execute(query)
        mydb.commit()
    except Error as err:
        print(f"Error: '{err}'")

def insert_query(query, val):
    cursor = mydb.cursor()
    try:
        cursor.execute(query, val)
        mydb.commit()
        return True
    except Error as err:
        print(f"Error: '{err}'")
        return False

def read_query(query):
    cursor = mydb.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")