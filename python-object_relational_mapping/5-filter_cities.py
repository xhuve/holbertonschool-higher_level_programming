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
                 ORDER BY cities.id
                 HAVING states.name = %s""", (argv[4],))

    rows = curr.fetchall()

    for row in range(len(rows)):
        print(rows[row])

    curr.close()
    db.close()
