#!/usr/bin/python3
"""List Module"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])

    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
                        ORDER BY id ASC", (argv[4], ))
    result = mycursor.fetchall()
    for result in result:
        print(result)
    mycursor.close()
    database.close()
