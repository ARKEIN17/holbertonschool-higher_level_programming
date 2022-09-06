#!/usr/bin/python3
"""file that contains the class definition
    of a City and an instance
    Base = declarative_base():
    necesito mas lineas para que el codigo pase, que porqueria
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Starting the class"""
    __tablename__ = 'cities'
    id = Column(Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey("states_id"))
