#!/usr/bin/python3
"""
A Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Connects to the DB and retrieves all states
    starting with N.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cur = db_connect.cursor()

    db_cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    lst = db_cur.fetchall()
    for item in lst:
        print(item)
