#!/usr/bin/python3
""" Import modules """
import sys
import MySQLdb


""" Main function  """


def main():

    """ Main function  """
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    searched = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=dbname, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s \
    ORDER BY states.id ASC"
    cur.execute(query, (searched,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
