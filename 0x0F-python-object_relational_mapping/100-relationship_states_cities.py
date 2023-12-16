#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco"
   in the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create(username, password, db_name):
    """Create the State "California" with the City
    "San Francisco" in the database"""
    DB_URL = f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    addState = State(name='California')
    addCity = City(name='San Francisco')
    session.add(addState)
    session.add(addCity)
    addState.cities.append(addCity)
    session.commit()

    session.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]
    create(username, password, db_name)
