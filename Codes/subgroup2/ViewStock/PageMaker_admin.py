import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import sqlite3

win = Tk()
win.title("어드민")
win.geometry("700x320+300+100") #가로 * 세로 + x좌표 + y좌표

a = StringVar()
b = StringVar()

def Select():
    conn = sqlite3.connect("DB.db") 
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM SalesData")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert('', 'end', values=row)
    conn.commit()


#재고 프레임
frame_opt = LabelFrame(win, text="재고상황")
frame_opt.pack(fill = "x", padx=5, pady=5)


#지점
brand_lbl = Label(frame_opt, text="지점 :")
brand_lbl.pack(side="left",padx=2, pady=5)

list1 = ['서교동','연희동','진관동','여의도동','신사동'];
 
droplist=OptionMenu(frame_opt,a, *list1)
droplist.config(width=15)
a.set('지점을 선택하세요.') 
droplist.pack(side="left",padx=2, pady=5)

#창고
brand_lbl = Label(frame_opt, text="창고 :")
brand_lbl.pack(side="left",padx=2, pady=5)

list2 = ['마포구','서대문구','은평구','영등포구','강남구'];
 
droplist=OptionMenu(frame_opt,b, *list2)
droplist.config(width=15)
b.set('창고를 선택하세요.') 
droplist.pack(side="left",padx=2, pady=5)

#지점 선택
select = Button(frame_opt, text='선택',width=5,bg='brown',fg='white',command=Select)
select.pack(side="left",padx=10, pady=5)


tree= ttk.Treeview(win,column=("column1", "column2", "column3","column4"), show='headings')

tree.column("#1", width=70, anchor="center")
tree.heading("column1", text="지점명", anchor="c")

tree.column("#2", width=100,anchor="c")
tree.heading("column2", text="브랜드명",anchor="c")

tree.column("#3", width=100, anchor="c")
tree.heading("column3", text="상품명", anchor="c")

tree.column("#4", width=100, anchor="center")
tree.heading("column4", text="판매수량", anchor="c")
tree.pack(fill="x")

win.mainloop()
