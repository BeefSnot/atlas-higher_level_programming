#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
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

    # Query the first State object based on states.id
    first_state = session.query(State).order_by(State.id).first()

    # Check if a state was found and print it, otherwise print "Nothing"
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()