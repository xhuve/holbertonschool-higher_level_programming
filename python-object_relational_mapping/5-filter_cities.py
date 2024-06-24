#!/usr/bin/python3
"""SQL learning"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """SQL Learning"""

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    curr = db.cursor()

    curr.execute("""SELECT cities.name FROM cities
                 INNER JOIN states ON cities.state_id = states.id
                 WHERE states.name = %s
                 ORDER BY cities.id""", (argv[4],))

    rows = curr.fetchall()

    for row in range(len(rows)):
        if row == len(rows) - 1:
            print(rows[row][0], end="")
        else:
            print(rows[row][0], end=', ')
    print()

    curr.close()
    db.close()
