#!/usr/bin/python3
"""SQL learning"""

import sys
import MySQLdb

if __name__ == '__main__':
    """SQL Learning"""

    print(sys.argv[1])

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    curr = db.cursor()

    s = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(sys.argv[4])

    curr.execute(s)

    rows = curr.fetchall()

    for row in range(len(rows)):
        print(row)

    curr.close()
    db.close()
