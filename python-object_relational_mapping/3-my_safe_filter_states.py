#!/usr/bin/python3
"""SQL learning"""

import sys
import MySQLdb

if __name__ == '__main__':
    """SQL Learning"""

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    curr = db.cursor()

    curr.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id".format(sys.argv[4]))

    rows = curr.fetchall()

    for row in rows:
        print(row[0])

    curr.close()
    db.close()
