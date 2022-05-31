import sqlite3, time
from datetime import datetime

def connection():
    return sqlite3.connect('Gymboard.db')


def tags(parent_id):
    con = connection()
    cur = con.cursor()
    tags = []
    cur.execute("SELECT id, name FROM tags WHERE parent_id = %d;" % (parent_id))
    for dsatz in cur:
        tags.append(list(dsatz))
    con.close()
    return tags

def documents_light(tags_id):
    con = connection()
    cur = con.cursor()
    documents = []
    cur.execute("SELECT id, name FROM documents WHERE tags_id = %d;" % (tags_id))
    for dsatz in cur:
        documents.append(list(dsatz))
    con.close()
    return documents
