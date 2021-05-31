import tkinter.ttk as ttk
from tkinter import *
import sqlite3


def Select():
    conn = sqlite3.connect("DB.db") 
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM SalesData")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert('', 'end', values=row)
    conn.commit()
