import sqlite3
import pandas as pd

def connect():
    conn=sqlite3.connect("cm.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS maintenance (code TEXT PRIMARY KEY, service TEXT,duree INTEGER, detail TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS calendrier (id INTEGER PRIMARY KEY, date DATE, code TEXT, FOREIGN KEY (code) REFERENCES maintenance (code))")
    conn.commit()
    conn.close()

def insert_m(code,service,duree,detail):
    conn=sqlite3.connect("cm.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO maintenance VALUES (?,?,?,?)",(code,service,duree,detail))
    conn.commit()
    conn.close()
def insert_c(date,code):
    conn=sqlite3.connect("cm.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO calendrier VALUES (NULL,?,?)",(date,code))
    conn.commit()
    conn.close()

#insert_m("RD01","DET",30,"verifier l'alimentation du ventilateur")
#insert_c("23/06/2020","TR01")
#insert_c("28/06/2020","TR01")


def view_m():
    conn=sqlite3.connect("cm.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM maintenance")
    rows=cur.fetchall()
    conn.close()
    return rows
def view_c():
    conn=sqlite3.connect("cm.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM calendrier")
    rows=cur.fetchall()
    conn.close()
    return rows

#print(view_c())
#print(view_m())

def searchS(service=""):
    conn=sqlite3.connect("cm.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM maintenance WHERE service=?", (service,))
    rows=cur.fetchall()
    conn.close()
    return rows

def searchD(service=""):
    conn=sqlite3.connect("cm.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM maintenance WHERE service=?", (service,))
    rows=cur.fetchall()
    conn.close()
    return rows


connect()

#print(search("TRANS"))


def droptable():
    conn1=sqlite3.connect("cm.db")
    cur1=conn1.cursor()
    cur1.execute("DROP TABLE IF EXISTS calendrier")
    conn1.commit()
    conn1.close()
