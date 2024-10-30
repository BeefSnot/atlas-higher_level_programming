#!/usr/bin/python3
"""
Contains the class definition of a State and an instance of Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create instance of Base from declarative_base
Base = declarative_base()

class State(Base):
    """
    Class representing a State in the database, linked to the 'states' table.
    """
    __tablename__ = 'states'

    # Auto-generated, unique integer id, primary key
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # Name of the state, max 128 characters, can't be null
    name = Column(String(128), nullable=False)