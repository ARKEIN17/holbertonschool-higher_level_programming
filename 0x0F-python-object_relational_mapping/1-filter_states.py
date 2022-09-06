#!/usr/bin/python3
"""List Module"""

from sqlite3 import Row
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])

    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM states \
                        WHERE name LIKE BINARY 'N%' ORDER BY id;")
    result = mycursor.fetchall()
    for result in result:
        if result[1][0] == "N":
            print(result)
    mycursor.close()
    database.close()
