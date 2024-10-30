#!/usr/bin/python3
"""
Script that lists all cities of a given state in the database hbtn_0e_4_usa.
The state name is provided as an argument (SQL injection free).
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to get cities for the given state
    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    
    cursor.execute(query, (state_name,))

    # Fetch all the results
    cities = cursor.fetchall()

    # Print the city names in a comma-separated format
    print(", ".join([city[0] for city in cities]))

    # Close the cursor and database connection
    cursor.close()
    db.close()