#!/usr/bin/python3
"""
return all table values (table 'states')
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    userName = argv[1]
    password = argv[2]
    databaseName = argv[3]

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port="3306",
                         user=userName,password=password,
                         db=databaseName)

    cur = db.cursor()
    cur.execute("SELECT * states WHERE\
                name LIKE BINARY 'N%' ORDER BY id ASC")

    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)
    cur.close()
    db.close()
