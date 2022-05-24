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
    cur = con.cursor()

    cur.execute("SELECT * FROM comments WHERE id_Comment = %d ORDER BY datum DESC;" % (comment))
    for dsatz in cur:
        cdsatz = (list(dsatz))
        comments.append(cdsatz)

    return comments
    con.close()

def searchDocument(tag):
    con = connection()
    cur = con.cursor()
    documents = []
    #sql = """SELECT documents.name FROM tags_Documents
            #JOIN documents
            #ON tags_Documents.id_Document = documents.id
            #WHERE tags_Documents.id_Tag = 1;"""  #SELECT documents.* geht aber documents.name nicht!
    sql = """SELECT documents.name FROM documents
             JOIN tags_Documents
             ON documents.id = tags_Documents.id_Document"""

    cur.execute(sql)
    for dsatz in cur:
        documents.append(dsatz)
    con.close()
    return documents


def tags(level):
    con = connection()
    cur = con.cursor()
    tags = []
    cur.execute("SELECT name FROM tags WHERE level = %d" % (level))
    for dsatz in cur:
        tags.append(list(dsatz))
    con.close()
    return tags




print(tags(0))
