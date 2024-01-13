#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_4_usa """
import sys
import MySQLdb


def connect():
    """ connect to database """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[
        2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            where states.name = %s""", (sys.argv[4], ))
    rows = cur.fetchall()
    for row in range(len(rows)):
        print(rows[row][0], end='')
        if (row != len(rows) - 1):
            print(end=', ')
        else:
            print()
    cur.close()
    db.close()


if __name__ == "__main__":
    connect()
