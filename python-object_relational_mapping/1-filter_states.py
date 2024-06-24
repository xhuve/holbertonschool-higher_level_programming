#!/usr/bin/python3
"""SQL learning"""

import sys
import MySQLdb

if __name__ == '__main__':
    """SQL Learning"""

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    curr = db.cursor()

    curr.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = curr.fetchall()

    print(rows)

    curr.close()
    db.close()

