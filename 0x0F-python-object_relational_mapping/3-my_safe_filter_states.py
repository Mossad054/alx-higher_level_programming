#!/usr/bin/python3
"""
Module to connects  python script to database
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

    # Creates cursor object to interact with the database
    my_cursor = my_db.cursor()

    # Executes SELECT query to fetch data.
    my_cursor.execute(
        "SELECT * FROM states  WHERE name=%s ORDER BY id", (argv[4], ))

    # Fetches all  data returned by the query
    my_data = my_cursor.fetchall()

    # Iterate through fetched data and print each row
    for row in my_data:
        print(row)

    # Close all cursors.
    my_cursor.close()

    # Close all databases
    my_db.close()
