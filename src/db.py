from sqlite3 import connect
import mysql.connector
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

host = os.environ.get("DATABASE_HOST") or 'localhost'
username = os.environ.get("DATABASE_USERNAME") or 'admin'
password = os.environ.get("DATABASE_PASSWORD") or 'root'
databaseName = os.environ.get("DATABASE_PASSWORD") or 'database'

mydb = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=databaseName
)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def insert_users(connection, val):
    user_sql = '''
    INSERT INTO USERS (ID, NAME, SCREEN_NAME, DESCRIPTION, LANG, PROFILE_IMAGE_URL, GENDER, AGE_GROUP, IS_ORG) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        execute_list_query(connection, user_sql, val)
    except Error as err:
        print(f"Error: '{err}'")
    
def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
    except Error as err:
        print(f"Error: '{err}'")