#!/usr/bin/python3
"""Lists all states  starting with ‘N’ from the database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port="3306",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE\
                name LIKE BINARY 'N%' ORDER BY states.id ASC".format(sys.argv[4]))

    all = cur.fetchall()
    for row in all:
        print(row)

    cur.close()
    db.close()
