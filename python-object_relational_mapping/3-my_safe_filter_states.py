#!/usr/bin/python3


import MySQLdb
from sys import argv


if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port="3306",
                         user=argv[1],
                         password=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name=%s ORDER BY states.id ASC", (argv[4],))

    all = cur.fetchall()
    for row in all:
        print(row)
    cur.close()
    db.close()
