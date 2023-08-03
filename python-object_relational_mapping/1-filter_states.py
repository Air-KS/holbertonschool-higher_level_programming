#!/usr/bin/python3
"""
Lists all states  starting with ‘N’
from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(
        host="localhost",
        port="3306",
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # Cursor
    cur = db.cursor()

    # Exécute une requête SQL
    cur.execute(
        "SELECT * FROM states \
         WHERE name \
         LIKE BINARY 'N%' ORDER BY states.id ASC"
    )

    all = cur.fetchall()
    for row in all:
        print(row)

    cur.close()
    db.close()
