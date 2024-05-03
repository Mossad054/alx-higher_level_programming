#!/usr/bin/python3
"""
Modules to connect  script to a database
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

    # Creates cursor object to interact with a database
    my_cursor = my_db.cursor()

    # Execute SELECT query to fetch data
    my_cursor.execute(
        """
        SELECT * FROM states  WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC
        """.format(argv[4])
        )

    # fetch data returned by the query
    my_data = my_cursor.fetchall()

    # Iterate thru fetched data and print each row
    for row in my_data:
        print(row)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()
