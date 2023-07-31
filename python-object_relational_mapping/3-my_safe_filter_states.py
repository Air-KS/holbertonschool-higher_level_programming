#!/usr/bin/python3
""" SQL injection to delete all record of a table"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    
    # connect to database
    db = MySQLdb.connect(
        host="localhost", port="3306",
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # Cursor
    cur = db.cursor()

    # Exécute une requête SQL
    cur.execute(
        "SELECT * FROM states \
        WHERE name=%s \
        ORDER BY states.id ASC", (argv[4],)
    )

    states = cur.fetchall()
    for row in states:
        print(row)

    cur.close()
    db.close()
