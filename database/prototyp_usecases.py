import sqlite3, time
from datetime import datetime

def connection():
    return sqlite3.connect('Gymboard.db')


def tags(level):
    con = connection()
    cur = con.cursor()
    tags = []
    cur.execute("SELECT name FROM tags WHERE level = %d" % (level))
    for dsatz in cur:
        tags.append(list(dsatz))
    con.close()
    return tags
