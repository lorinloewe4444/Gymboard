import sqlite3



def modell():
    con = sqlite3.connect('GymBoard.db')
    cur = con.cursor()

    sql = "SELECT * FROM users"
    cur.execute(sql)
    for dsatz in cur:
        print(dsatz)
    con.close()



# Count Likes from a specific Document
def countLikesDoc(id_Document):
    likes = 0

    con = sqlite3.connect('GymBoard.db')
    cur = con.cursor()

    cur.execute("SELECT id FROM likes where id_Document = (?)" , (id_Document))
    for dsatz in cur:
        likes += 1
    return likes
    con.close()

# Count Likes from a specific comment
def countLikesCom(id_Comment):
    likes = 0

    con = sqlite3.connect('GymBoard.db')
    cur = con.cursor()

    cur.execute("SELECT id FROM likes where id_Document = (?)" , (id_Comment))
    for dsatz in cur:
        likes += 1
    return likes
    con.close()

# Returns a list of the comments from a specific document
def commentsDocument(document):
    

print(countLikesCom('3'))
