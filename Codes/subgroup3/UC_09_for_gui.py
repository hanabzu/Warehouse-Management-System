from tkinter import *
from UC_09_ShopkeeperOrder import *

root = Tk()
root.title("shopkeeperOrder")
root.geometry("540x380+100+200")
root.resizable(False,False)


btn_s = Button(root, width = 10, height = 2,text = "점주", command=controller.initiator())
btn_wh = Button(root, width = 10, height = 2, text = "창고주")

btn_s.pack()
btn_wh.pack()

root.mainloop()