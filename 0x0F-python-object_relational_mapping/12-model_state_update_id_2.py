#!/usr/bin/python3
"""prints the State"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    database = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    sesion = Session(database)
    sesion.query(State).filter(State.id == 2).update(
        {State.name: 'New Mexico'}, synchronize_session=False)
    sesion.commit()
