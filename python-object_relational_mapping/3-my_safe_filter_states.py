#!/usr/bin/python3
"""SQL learning"""

import sys
import MySQLdb

if __name__ == '__main__':
    """SQL Learning"""

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    curr = db.cursor()

    rows = curr.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id".format(sys.argv[4]))

    for row in rows:
        print(row)

    curr.close()
    db.close()
