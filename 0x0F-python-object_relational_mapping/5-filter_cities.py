#!/usr/local/bin/python3
""" Import modules """
import sys
import MySQLdb

""" Main function  """


def main():
    """ Main function  """
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    stateName = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=dbname, charset="utf8")
    cur = conn.cursor()
    query = " SELECT name FROM cities WHERE cities.state_id =\
        (SELECT id FROM states WHERE name = %s)"
    cur.execute(query, (stateName,))
    query_rows = cur.fetchall()
    data = ''
    for row in query_rows:
        data += ', '.join(row) + ', '
    data = data.rstrip(" ,")
    print(data)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
