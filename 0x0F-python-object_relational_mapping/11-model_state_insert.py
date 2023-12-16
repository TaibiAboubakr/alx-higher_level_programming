#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, text)
from sqlalchemy.orm import sessionmaker


def main(username, password, dbname):
    """ function that execute the query  """
    DB_URL = f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}'
    engine = create_engine(DB_URL)
    session = sessionmaker(bind=engine)()
    new_State = State(name='Louisiana')
    session.add(new_State)
    session.commit()


if __name__ == "__main__":
    username, password, dbname = sys.argv[1:]
    main(username, password, dbname)
