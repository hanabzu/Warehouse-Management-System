

from tkinter import *
from tkinter.ttk import *
import sqlite3


con = sqlite3.connect("Stock.db")
cur = con.cursor()




cur.execute("CREATE TABLE Stock (name TEXT, stock INTEGER)")
cur.execute("INSERT INTO Stock VALUES ('새우깡', 123)")
 
class StockData(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
 
        self.master = master
        self.master.title("재고 정보")
        self.pack(fill=BOTH, expand=True)

        def add():
            name = Entry.get(entryname)
            stock = Entry.get(entrystock)
            cur.execute("INSERT INTO Stock values(?,?);",(str(name),int(stock)))
            con.commit()

        def edit():
            name = Entry.get(entryname)
            stock = Entry.get(entrystock)
            cur.execute("UPDATE Stock SET stock = ? WHERE name = ?",(int(stock),str(name)))
            con.commit()

        def delete():
            name = Entry.get(entryname)
            stock = Entry.get(entrystock)
            cur.execute("DELETE FROM Stock WHERE name = ?" ,(str(name),))
            con.commit()
 
        # 재품
        frame1 = Frame(self)
        frame1.pack(fill=X)
 
        lblname = Label(frame1, text="제품명", width=10)
        lblname.pack(side=LEFT, padx=10, pady=10)
 
        entryname = Entry(frame1)
        entryname.pack(fill=X, padx=10, expand=True)
 
        # 재고량
        frame2 = Frame(self)
        frame2.pack(fill=X)
 
        lblstock = Label(frame2, text="재고량", width=10)
        lblstock.pack(side=LEFT, padx=10, pady=10)
 
        entrystock = Entry(frame2)
        entrystock.pack(fill=X, padx=10, expand=True)


        # 추가
        frame3 = Frame(self)
        frame3.pack(fill=X)
        btnAdd = Button(frame3, text="추가", command=add)
        btnAdd.pack(side=LEFT, padx=10, pady=10)

        # 수정
        frame4 = Frame(self)
        frame4.pack(fill=X)
        btnEdit = Button(frame4, text="수정", command=edit)
        btnEdit.pack(side=LEFT, padx=10, pady=10)

        # 삭제
        frame5 = Frame(self)
        frame5.pack(fill=X)
        btnDelete = Button(frame5, text="삭제", command=delete)
        btnDelete.pack(side=LEFT, padx=10, pady=10)


 
 
def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = StockData(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

