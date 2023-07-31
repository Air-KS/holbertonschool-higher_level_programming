#!/usr/bin/python3

"""Lists all states  starting with ‘N’ from the database hbtn_0e_0_usa"""
import mysql.connector
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = mysql.connector.connect(host="localhost",
                                 port="3306",
                                 user=argv[1],
                                 password=argv[2],
                                 db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE\
                name LIKE BINARY 'N%' ORDER BY states.id ASC")

    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)

    cur.close()
    db.close()
