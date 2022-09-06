#!/usr/bin/python3
"""list all state of databace"""

from queue import Empty
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    database = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    sesion = Session(database)
    """Query to the database"""
    query = sesion.query(State).order_by(State.id)
    for instance in query:
        if "a" in instance.name:
            print(f"{instance.id}: {instance.name}")
