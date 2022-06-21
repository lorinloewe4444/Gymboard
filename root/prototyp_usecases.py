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
    return tags # [tags.id, tags.name]

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
    return documents #[documents.id, documents.id_Users, documents.name, documents.path, documents.datum, documents.id_Tags, users.nickName, COUNT(likes)]

def comments(id_Document):
    con = connection()
    cur = con.cursor()
    comments = []
    cur.execute("SELECT comments.*, users.nickName FROM comments JOIN users ON users.id = comments.id_User WHERE comments.id_Document = %d AND comments.id_Comment IS NULL" % (id_Document))
    for dsatz in cur:
        comments.append(list(dsatz))
    con.close()
    return comments #[comments.id, comments.id_Comment, comments.id_Document, comments.id_User, comments.comment, comments.datum, users.nickName]

def comments_rec(id_Comment):
    con = connection()
    cur = con.cursor()
    comments = []
    cur.execute("SELECT comments.*, users.nickName FROM comments JOIN users ON users.id = comments.id_User WHERE comments.id_Document IS NULL AND comments.id_Comment =" % (id_Comment))
    for dsatz in cur:
        comments.append(list(dsatz))
    con.close()
    return comments #[comments.id, comments.id_Comment, comments.id_Document, comments.id_User, comments.comment, comments.datum, users.nickName]


def tags_docs(id_Parent):
    con = connection()
    cur = con.cursor()
    tags = []
    cur.execute("SELECT id, name FROM tags WHERE id_Parent = %d;" % (id_Parent))
    for dsatz in cur:
        tags.append(list(dsatz))
    documents = []
    cur.execute("SELECT id, name, datum FROM documents WHERE id_Tags = %d;" % (id_Parent))
    for dsatz in cur:
        dsatz = list(dsatz)
        dsatz[-1] = datetime.fromtimestamp(dsatz[-1]).strftime('%Y/%m/%d')
        documents.append(dsatz)
    con.close()
    return [tags, documents] # [[tags.id, tags.name], [documents.id, documents.name, documents.datum]]

if __name__ == "__main__":
    print(tags_docs(1010))
