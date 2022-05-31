import sqlite3, time
from datetime import datetime

def connection():
    return sqlite3.connect('Gymboard.db')


def tags(parent_id):
    con = connection()
    cur = con.cursor()
    tags = []
    cur.execute("SELECT name FROM tags WHERE parent_id = %d" % (parent_id))
    for dsatz in cur:
        tags.append(list(dsatz))
    con.close()
    return tags

print(tags(int(input())))
