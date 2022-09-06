#!/usr/bin/python3
"""List Module"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])

    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY id;")
    result = mycursor.fetchall()
    for value in result:
        print(value)
    mycursor.close()
    database.close()
