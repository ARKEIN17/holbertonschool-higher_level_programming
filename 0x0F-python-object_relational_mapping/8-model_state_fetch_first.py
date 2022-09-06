#!/usr/bin/python3
"""get firts state of databaces"""

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
    instance = sesion.query(State).first()
    if instance:
        print(f"{instance.id}: {instance.name}")
    else:
        print("Nothing")
