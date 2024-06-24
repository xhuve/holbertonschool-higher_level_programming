#!/usr/bin/python3
"""SQL learning"""

import sys
import MySQLdb

if __name__ == '__main__':
    """SQL Learning"""

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    curr = db.cursor()

    curr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    rows = curr.fetchall()

    for row in range(len(rows)):
        print(rows[row])

    curr.close()
    db.close()
