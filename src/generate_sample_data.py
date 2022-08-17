import request
import db
from datetime import datetime
from tqdm import tqdm

def setupDatabase():

    db_sql = '''
        CREATE DATABASE IF NOT EXISTS MLRouting
    '''
    db.execute_query(db_sql)
    print("Created database MLRouting")

    db.execute_query("USE MLRouting")

    table_sql = '''
        CREATE TABLE IF NOT EXISTS CallHistory (
            ID BIGINT NOT NULL,
            source VARCHAR(30),
            target VARCHAR(30),
            created DATETIME,
            direction VARCHAR(30),
            status VARCHAR(30),
            PRIMARY KEY (ID)    
        )
    '''

    db.execute_query(table_sql)
    print("Created table CallHistory")


def fillCallHistory(items):
    
    history_items_sql = '''
    INSERT INTO CallHistory (ID, SOURCE, TARGET, CREATED, DIRECTION, STATUS) 
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    db.execute_query("USE MLRouting")

    insert_count = 0
    for item in tqdm(items):
        item_tuple = (item["id"], item["source"], item["target"], datetime.strptime(item["created"], '%Y-%m-%dT%H:%M:%SZ'), item["direction"], item["status"])
        insert_successful = db.insert_query(history_items_sql, item_tuple)

        if insert_successful:
            insert_count += 1

    print(f'{insert_count} rows inserted!')


if __name__ == "__main__":
    print("Generating sample data")
    setupDatabase()

    fillCallHistory(request.getCallHistory(items=1000))
