#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, text)


def execute_query(username, password, dbname):
    """ function that execute the query  """
    DATABASE_URL = f'mysql://{username}:{password}@localhost:3306/{dbname}'
    engine = create_engine(DATABASE_URL)
    sql_query = text("select * from states;")
    with engine.connect() as connection:
        result = connection.execute(sql_query)
        for row in result:
            print(f"{row[0]}: {row[1]}")


if __name__ == "__main__":
    username, password, dbname = sys.argv[1:]
    execute_query(username, password, dbname)
