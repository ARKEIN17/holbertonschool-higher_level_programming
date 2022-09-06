#!/usr/bin/python3
"""List Module"""

from sqlite3 import Row
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect('localhost', argv[1],
                                    argv[2], argv[3])

    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM states \
                        WHERE name LIKE BINARY 'N%' ORDER BY id;")
    result = mycursor.fetchall()
    for result in result:
        if result[1][0] == "N":
            print(result)
    mycursor.close()
    database.close()
