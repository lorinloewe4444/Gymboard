import sqlite3, time
from datetime import datetime

def connection():
    return sqlite3.connect('Gymboard.db')

def modell():
    con = connection()
    cur = con.cursor()

    sql = "SELECT * FROM users"
    cur.execute(sql)
    for dsatz in cur:
        print(dsatz)
    con.close()



# Count Likes from a specific Document
def countLikesDoc(id_Document):
    likes = 0

    con = connection()
    cur = con.cursor()

    cur.execute("SELECT COUNT(id) FROM likes WHERE id_Document = %d;" % (id_Document))
    for dsatz in cur:
        likes = dsatz

    con.close()
    return likes


# Count Likes from a specific comment
def countLikesCom(id_Comment):
    likes = 0

    con = connection()
    cur = con.cursor()

    cur.execute("SELECT id FROM likes WHERE id_Document = %d;" % (id_Comment))
    for dsatz in cur:
        likes += 1
    return likes
    con.close()

# Returns a list of the comments from a specific document
def commentsDocument(document):
    comments = []
    con = connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM comments WHERE id_Document = %d AND id_Comment IS NULL ORDER BY datum DESC;" % (document))
    for dsatz in cur:
        cdsatz = (list(dsatz))
        comments.append(cdsatz)

    return comments
    con.close()

def commentsComment(comment):
    comments = []

    con = connection()


print(commentsDocument(2))
