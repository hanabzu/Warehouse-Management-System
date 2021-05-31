from UC_09_ShopkeeperOrder.controller import initiator
from tkinter import *
from UC_09_ShopkeeperOrder import *

root = Tk()
root.title("shopkeeperOrder")
root.geometry("540x380+100+200")
root.resizable(False,False)

def initiate_s():
    global ctrl
    ctrl = controller.initiator(2).return_controller()
    btn_s.pack_forget()
    btn_wh.pack_forget()
    btn_order_request.pack()
    btn_order_result_check.pack()
def initiate_wh():
    global ctrl
    ctrl = controller.initiator(1).return_controller()

def MakeOrder():
    order_list = ctrl.MakeOrder()
    order_sender = OrderSender.OrderSender(order_list, ctrl.user.connected, ctrl.user.id ,ctrl.user.type)
    order_sender.SendOrder()

btn_s = Button(root, width = 10, height = 2,text = "점주", command=initiate_s)
btn_wh = Button(root, width = 10, height = 2, text = "창고주", command=initiate_wh)

btn_order_request = Button(root, width = 15, height= 2, text = "발주 신청", command=MakeOrder)
btn_order_result_check = Button(root, width= 15, height=2,text = "발주 결과 확인")

btn_s.pack()
btn_wh.pack()

root.mainloop()


