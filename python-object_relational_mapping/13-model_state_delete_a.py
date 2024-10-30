
#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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

    # Query and delete all states containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
