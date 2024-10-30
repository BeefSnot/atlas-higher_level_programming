#!/usr/bin/python3
"""
Script that fetches and prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
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

    # Query to fetch all cities with their corresponding states
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Display the results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()