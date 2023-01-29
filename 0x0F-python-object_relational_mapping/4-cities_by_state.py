#!/usr/bin/python3
"""
A Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Connects to the databases and retrieves list
    of all cities.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )

    db_cur = db_connect.cursor()

    db_cur.execute("SELECT cities.id, cities.name, states.name\
        FROM cities JOIN states ON cities.state_id\
            = states.id ORDER BY cities.id")

    lst = db_cur.fetchall()
    for item in lst:
        print(item)
