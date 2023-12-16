#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, text)
from sqlalchemy.orm import sessionmaker


def main(username, password, dbname, StateName):
    """ function that execute the query  """
    DB_URL = f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}'
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name.like(StateName)).first()
    if results is None:
        print("Not found")
    else:
        print(results.id)


if __name__ == "__main__":
    username, password, dbname, StateName = sys.argv[1:]
    main(username, password, dbname, StateName)
