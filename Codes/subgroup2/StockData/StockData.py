

from tkinter import *
from tkinter.ttk import *
 
class StockData(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
 
        self.master = master
        self.master.title("재고 정보")
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
 
        lblComp = Label(frame2, text="재고량", width=10)
        lblComp.pack(side=LEFT, padx=10, pady=10)
 
        entryComp = Entry(frame2)
        entryComp.pack(fill=X, padx=10, expand=True)


        # 수정
        frame3 = Frame(self)
        frame3.pack(fill=X)
        btnEdit = Button(frame3, text="수정")
        btnEdit.pack(side=BOTTOM, padx=10, pady=10)


 
 
def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = StockData(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

