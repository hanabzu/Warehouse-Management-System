import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import sqlite3

win = Tk()
win.title("점주")
win.geometry("700x430+300+100") #가로 * 세로 + x좌표 + y좌표

#1. 판매 내역 프레임
frame_opt = LabelFrame(win, text="판매내역")
frame_opt.pack(fill = "x", padx=5, pady=5)

#지점
brand_lbl = Label(frame_opt, text="지점 :")
brand_lbl.pack(side="left",padx=2, pady=5)

list1 = ['서교동','연희동','진관동','여의도동','신사동'];
 
droplist=OptionMenu(frame_opt,c, *list1)
droplist.config(width=15)
c.set('지점을 선택하세요.') 
droplist.pack(side="left",padx=2, pady=5)

#지점 선택
select = Button(frame_opt, text='선택',width=5,bg='brown',fg='white',command=Select)
select.pack(side="left",padx=10, pady=5)

#2. 상품 추가 프레임
frame_add = LabelFrame(win, text="상품 추가")
frame_add.pack(fill = "x", padx=5, pady=5)

#브랜드
brand_lbl = Label(frame_add, text="브랜드 :")
brand_lbl.pack(side="left",padx=2, pady=5)

brand_entry = Entry(frame_add,textvar=Fullname)
brand_entry.pack(side="left",padx=2, pady=5)

#상품
product_lbl = Label(frame_add, text="상품 :")
product_lbl.pack(side="left",padx=2, pady=5)

product_entry = Entry(frame_add,textvar=Goods)
product_entry.pack(side="left",padx=2, pady=5)

#판매수량
count_lbl = Label(frame_add, text="판매수량 :")
count_lbl.pack(side="left",padx=2, pady=5)

count_entry = Entry(frame_add,textvar=var)
count_entry.pack(side="left",padx=2, pady=5)

#추가
insert = Button(frame_add, text='추가',width=5,bg='brown',fg='white',command=Insert)
insert.pack(side="left",padx=10, pady=5)

#get = Button(frame_add, text='get',width=5,bg='brown',fg='white',command=Get)
#get.pack(side="left",padx=10, pady=5)

frame_tr = LabelFrame(win, text="")
frame_tr.pack(fill = "x", padx=5, pady=5)

tree= ttk.Treeview(frame_tr,column=("column1", "column2", "column3","column4"), show='headings')


tree.column("#1", width=70, anchor="center")
tree.heading("column1", text="지점명", anchor="c")

tree.column("#2", width=100,anchor="c")
tree.heading("column2", text="브랜드명",anchor="c")

tree.column("#3", width=100, anchor="c")
tree.heading("column3", text="상품명", anchor="c")

tree.column("#4", width=100, anchor="center")
tree.heading("column4", text="판매수량", anchor="c")

tree.pack(fill="x")

frame_btn = LabelFrame(win, text="")
frame_btn.pack(side="right", padx=5, pady=2)

#삭제
delete = Button(frame_btn, text='삭제',width=5,bg='brown',fg='white',command=Delete)
delete.pack(side="right",padx=5, pady=5)

#수정
update = Button(frame_btn, text='수정',width=5,bg='brown',fg='white',command=Update)
update.pack(side="right",padx=10, pady=5)



win.mainloop()
