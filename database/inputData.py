import sqlite3
import string
import random

table = "users"

sql = """INSERT INTO users(eMail, nickName, status, role, datum)
VALUES('asterix.gallien@stud.gyminterlaken.ch', 'asterix', 0, 0, '1651587175')"""


def addData(table, amount):

    con = sqlite3.connect('GymBoard.db')
    cur = con.cursor()

    if table == "users":
        print(table)
        for i in range(0, amount):
            nickName = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
            eMail = nickName + "."+''.join(random.choice(string.ascii_uppercase) for _ in range(8))+"@stud.gyminterlaken.ch"
            datum = 1092941466 + random.randrange(-100, -2)
            sql = """INSERT INTO %s(eMail, nickName, status, role, datum)
            VALUES('%s', '%s', 0, 0, %d)""" %(table, eMail, nickName, datum)
            cur.execute(sql)
            print("added")
            con.commit()

    elif table == "documents":
        print("documents")
        for i in range(0, amount):
            sql = """SELECT id FROM users
                    ORDER BY random()
                    LIMIT 1;"""
            cur.execute(sql)
            id_User = cur.fetchone()[0]
            name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
            path = ''.join(random.choice(string.ascii_letters) for _ in range(18))
            datum = 1092941466 + random.randrange(-10, -1)
            sql = """INSERT INTO %s(id_User, name, path, datum)
            VALUES(%d, '%s', '%s', %d)""" %(table, id_User, name, path, datum)
            print (sql)



    elif table == "comments":
        print("f")

    else:
        print("invalid table")





    con.close()

addData(table, 5)


#def addTags():


#addTags()
