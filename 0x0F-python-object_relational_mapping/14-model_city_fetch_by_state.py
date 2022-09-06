#!/usr/bin/python3
"""prints the State"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    database = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    sesion = Session(database)
    query = sesion.query(State, City).filter(City.state_id == State.id).order_by(City.id).all()
    for state_instance, city_instance in query:
        print(f"{state_instance.name}: ({city_instance.id}) {city_instance.name}")
