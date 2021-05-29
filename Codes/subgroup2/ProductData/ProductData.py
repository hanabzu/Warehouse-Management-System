from tkinter import *
from tkinter.ttk import *
 
class ProductData(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
 
        self.master = master
        self.master.title("제품 정보")
        self.pack(fill=BOTH, expand=True)
 
        # 성명
        frame1 = Frame(self)
        frame1.pack(fill=X)
 
        lblName = Label(frame1, text="제품명", width=10)
        lblName.pack(side=LEFT, padx=10, pady=10)
 
        entryName = Entry(frame1)
        entryName.pack(fill=X, padx=10, expand=True)
 
        # 회사
        frame2 = Frame(self)
        frame2.pack(fill=X)
 
        lblComp = Label(frame2, text="브랜드명", width=10)
        lblComp.pack(side=LEFT, padx=10, pady=10)
 
        entryComp = Entry(frame2)
        entryComp.pack(fill=X, padx=10, expand=True)
 
 
        # 추가
        frame3 = Frame(self)
        frame3.pack(fill=X)
        btnAdd = Button(frame3, text="추가")
        btnAdd.pack(side=LEFT, padx=10, pady=10)

        # 수정
        frame4 = Frame(self)
        frame4.pack(fill=X)
        btnEdit = Button(frame4, text="수정")
        btnEdit.pack(side=LEFT, padx=10, pady=10)

        # 삭제
        frame5 = Frame(self)
        frame5.pack(fill=X)
        btnDelete = Button(frame5, text="삭제")
        btnDelete.pack(side=LEFT, padx=10, pady=10)
 
 
def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = ProductData(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

