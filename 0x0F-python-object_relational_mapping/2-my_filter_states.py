#!/usr/bin/python3
"""
A Script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Connects to the DB and retrieves the state
    passed in as an arg.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cur = db_connect.cursor()

    db_cur.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))

    lst = db_cur.fetchall()
    for item in lst:
        print(item)
