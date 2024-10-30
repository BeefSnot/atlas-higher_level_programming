#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and connect to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Create a configured session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")

    # Add the new state to the session and commit
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()