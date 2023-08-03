#!/usr/bin/python3
""" SQL injection to delete all record of a table"""

import MySQLdb
import sys

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(
        host="localhost", port="3306",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # Create cursor to execute using SQL; join two tables for all info
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM states \
                 INNER JOIN cities ON states.id = cities.state_id \
                 ORDER BY cities.id ASC ")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
