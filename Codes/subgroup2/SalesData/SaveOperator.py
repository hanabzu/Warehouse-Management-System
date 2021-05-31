import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import sqlite3

def Insert():
    if(name == "" or goods == "" or count == "" or country == ""):
        msgbox.showinfo("insert status", "ALL Fields are requires")
    else:
       conn = sqlite3.connect("DB.db") 
       cursor=conn.cursor()
       cursor.execute('CREATE TABLE IF NOT EXISTS SalesData (지점명 TEXT, 브랜드명 TEXT,상품명 TEXT,판매수량 INTEGER )')
       cursor.execute('INSERT INTO SalesData (지점명,브랜드명,상품명,판매수량) VALUES(?,?,?,?)',(country,name,goods,count,))
       msgbox.showinfo("insert status", "Inserted Successfully")
       conn.commit()

def Delete():
    conn = sqlite3.connect("DB.db") 
    cursor=conn.cursor()
    cursor.execute("DELETE FROM 'SalesData' WHERE 판매수량 = :country", {"country":1})
    msgbox.showinfo("delete status", "deleted Successfully")
    conn.commit()

def Update():
    conn = sqlite3.connect("DB.db") 
    cursor=conn.cursor()
    cursor.execute("UPDATE 'SalesData' SET 판매수량 = '%s' WHERE 상품명 = '%s'" % ('', '',))
    msgbox.showinfo("update status", "updated Successfully")
    conn.commit()

def Select():
    conn = sqlite3.connect("DB.db") 
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM SalesData")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
        tree.insert('', 'end', values=i, tags = "unchecked" )
    conn.commit()
