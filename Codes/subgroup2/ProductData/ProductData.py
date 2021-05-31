from tkinter import *
from tkinter.ttk import *
import sqlite3


con = sqlite3.connect("Product.db")
cur = con.cursor()




cur.execute("CREATE TABLE Product (name TEXT, brand TEXT)")
cur.execute("INSERT INTO Product VALUES ('새우깡', '농심')")





class ProductData(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
 
        self.master = master
        self.master.title("제품 정보")
        self.pack(fill=BOTH, expand=True)

        def add():
            name = Entry.get(entryname)
            brand = Entry.get(entrybrand)
            cur.execute("INSERT INTO Product values(?,?);",(str(name),str(brand)))
            con.commit()

        #def edit():
            #name = Entry.get(entryname)
            #brand = Entry.get(entrybrand)
            #cur.execute("INSERT INTO Product values(?,?);",(str(name),str(brand)))
            #con.commit()

        def delete():
            name = Entry.get(entryname)
            brand = Entry.get(entrybrand)
            cur.execute("DELETE FROM Product WHERE name = ? AND brand = ?", (str(name),str(brand)))
            con.commit()

        # 제품명
        frame1 = Frame(self)
        frame1.pack(fill=X)
 
        lblname = Label(frame1, text="제품명", width=10)
        lblname.pack(side=LEFT, padx=10, pady=10)
 
        entryname = Entry(frame1)
        entryname.pack(fill=X, padx=10, expand=True)    
 
        # 브랜드
        frame2 = Frame(self)
        frame2.pack(fill=X)
 
        lblbrand = Label(frame2, text="브랜드명", width=10)
        lblbrand.pack(side=LEFT, padx=10, pady=10)
 
        entrybrand = Entry(frame2)
        entrybrand.pack(fill=X, padx=10, expand=True)
 
 
        # 추가
        frame3 = Frame(self)
        frame3.pack(fill=X)
        btnAdd = Button(frame3, text="추가", command=add)
        btnAdd.pack(side=LEFT, padx=10, pady=10)

        # 수정
        #frame4 = Frame(self)
        #frame4.pack(fill=X)
        #btnEdit = Button(frame4, text="수정", command=edit)
        #btnEdit.pack(side=LEFT, padx=10, pady=10)

        # 삭제
        frame5 = Frame(self)
        frame5.pack(fill=X)
        btnDelete = Button(frame5, text="삭제", command=delete)
        btnDelete.pack(side=LEFT, padx=10, pady=10)

 
 
def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = ProductData(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
    
