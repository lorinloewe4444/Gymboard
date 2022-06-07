import sqlite3, time
from datetime import datetime

def connection():
    return sqlite3.connect('Gymboard.db')


def tags(id_Parent):
    con = connection()
    cur = con.cursor()
    tags = []
    cur.execute("SELECT id, name FROM tags WHERE id_Parent = %d;" % (id_Parent))
    for dsatz in cur:
        tags.append(list(dsatz))
    con.close()
    return tags

def documents_light(id_Tags):
    con = connection()
    cur = con.cursor()
    documents = []
    cur.execute("SELECT documents.id, documents.name FROM documents WHERE id_Tags = %d;" % (id_Tags))
    for dsatz in cur:
        documents.append(list(dsatz))
    for document in documents:
        cur.execute("SELECT COUNT(likes.id) FROM likes WHERE likes.id_Document = %d;" % (document[0]))
        for dsatz in cur:
            document.append(dsatz[0])
    con.close()
    return documents # [documents.id, documents.name, COUNT(likes)]

def documents(id_Tags):
    con = connection()
    cur = con.cursor()
    documents = []
    cur.execute("SELECT documents.*, users.nickName FROM documents JOIN users ON documents.id_User=users.id WHERE id_Tags = %d;" % (id_Tags))
    for dsatz in cur:
        documents.append(list(dsatz))
    for document in documents:
        cur.execute("SELECT COUNT(likes.id) FROM likes WHERE likes.id_Document = %d;" % (document[0]))
        for dsatz in cur:
            document.append(dsatz[0])
    con.close()
    return documents #[documents.id, documents.id_Users, documents.name, documents.path, documents.datum, documents.id_Tags, users.name, COUNT(likes)]

print(documents_light(1112))
