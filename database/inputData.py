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
        for i in range(0, amount):
            nickName = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
            eMail = nickName + "."+''.join(random.choice(string.ascii_uppercase) for _ in range(8))
            datum = 1092941466 + random.randrange(-50, -5)
            sql = """INSERT INTO %s(eMail, nickName, status, role, datum)
            VALUES(%s, %s, 0, 0, %d)""" %(table, eMail, nickName, datum)
            print (sql)
            print("finished")
    #con.execute(sql)
    #con.commit()
    else if table == "documents":
        for i in range(0, amount):
            sql = """SELECT title FROM albums
                    ORDER BY random()
                    LIMIT 5;"""
            cur.execute(sql)

            id_User =

    else if table == "comments":

    else:
        print("invalid table")


    con.close()

addData("users", 5)


def addTags():


addTags()
