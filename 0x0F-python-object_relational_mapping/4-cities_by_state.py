#!/usr/bin/python3
"""
Module to connect a python script to a database
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # Connects database using command-line arguments
    my_db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
    )

    # Create cursor object to interact with database
    my_cursor = my_db.cursor()

    # Execute SELECT query to fetch data.
    my_cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id"""
    )

    # fetch all data returned by the query
    my_data = my_cursor.fetchall()

    # Iterate via fetched data and print each row.
    for row in my_data:
        print(row)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()
