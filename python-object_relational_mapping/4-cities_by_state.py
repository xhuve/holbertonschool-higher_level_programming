#!/usr/bin/python3
"""SQL learning"""

import sys
import MySQLdb

if __name__ == '__main__':
    """SQL Learning"""

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    curr = db.cursor()

    curr.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states WHERE cities.state_id = states.id ORDER BY cities.id")

    rows = curr.fetchall()

    for row in range(len(rows)):
        print(rows[row])

    curr.close()
    db.close()
