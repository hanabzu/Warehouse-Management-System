from tkinter import *
from tkinter.ttk import *


con = sqlite3.connect("Product.db")
cur = con.cursor()




cur.execute("CREATE TABLE IF NOT EXISTS(name TEXT, brand TEXT)")





class ProductData(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
 
        self.master = master
        self.master.title("제품 정보")
        self.pack(fill=BOTH, expand=True)

        def add():
            cur.execute("insert into Product values(?,?);",(str(name),str(brand)))

        def exit():
            con.close()

        def edit():
            con.close()

        def delete():
            con.close()

        # 성명
        frame1 = Frame(self)
        frame1.pack(fill=X)
 
        name = Label(frame1, text="제품명", width=10)
        name.pack(side=LEFT, padx=10, pady=10)
 
        entryName = Entry(frame1)
        entryName.pack(fill=X, padx=10, expand=True)
 
        # 회사
        frame2 = Frame(self)
        frame2.pack(fill=X)
 
        brand = Label(frame2, text="브랜드명", width=10)
        brand.pack(side=LEFT, padx=10, pady=10)
 
        entryComp = Entry(frame2)
        entryComp.pack(fill=X, padx=10, expand=True)
 
 
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

        # 나가기
        frame6 = Frame(self)
        frame6.pack(fill=X)
        btnDelete = Button(frame6, text="나가기", command=exit)
        btnDelete.pack(side=LEFT, padx=10, pady=10)
 
 
def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = ProductData(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
    
