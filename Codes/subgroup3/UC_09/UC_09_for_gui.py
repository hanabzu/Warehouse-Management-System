from tkinter import *
from UC_09_ShopkeeperOrder import *
#mock up
root = Tk()
root.title("shopkeeperOrder")
root.geometry("1280x500+500+250")
root.resizable(False,False)
#stub
def view_stock():
    stock_file = open("stock_list.txt", "r", encoding="utf8")
    item_name = []
    item_brand = []
    item_price= []
    item_number = []
    while True:
        line = stock_file.readline()
        if not line:  # line이 없으면, 읽어올 라인이 없으면s
            break
        temp = line.split(' ')
        item_name.append(temp[0])
        item_brand.append(temp[1])
        item_price.append((int)(temp[2]))
        item_number.append((int)(temp[3]))

    print("{0: <20}{1: <20}{2: <20}{3: <20}".format("name", "brand", "price", "number"))
    for i in range(len(item_name)):
        print("{0: <20}{1: <20}{2: <20}{3: <20}".format(item_name[i],item_brand[i],item_price[i],item_number[i]))
    stock_file.close()
    return OrderList.OrderList(item_name,item_brand,item_price,item_number,0)

def initiate_s():
    btn_s.pack_forget()
    btn_wh.pack_forget()
    btn_order_request.pack()
    btn_order_result_check.pack()
def initiate_wh():
    btn_s.pack_forget()
    btn_wh.pack_forget()
    btn_order_check.pack()
    btn_exit.pack()

def MakeOrder():
    btn_order_request.pack_forget()
    btn_order_result_check.pack_forget()
    label1.pack(side="top")
    btn_complete.pack(side="bottom")
    # order_list = ctrl.MakeOrder()
    stock_list = view_stock()
    Label(frame_stock_list, text = "{0: <20}{1: <20}{2: <20}{3: <20}".format("item_name","item_brand","item_price","item_number")).pack()
    for i in range(len(stock_list.item_name)):
        Label(frame_stock_list, text = "{0: <20}{1: <20}{2: <20}{3: <20}".format(stock_list.item_name[i],stock_list.item_brand[i],stock_list.item_price[i],stock_list.item_number[i])).pack()
    frame_stock_list.pack(side="left",fill='both',expand=True)
    ent = Entry(frame_request, width=30)
    ent.insert(END,"name brand number 순으로 입력")
    ent.pack()
    btn_ok = Button(frame_request,width = 10, height=2, text="ok")
    btn_ok.pack()
    frame_request.pack(side="right",fill='both',expand=True)

    # order_sender = OrderSender.OrderSender(order_list, ctrl.user.connected, ctrl.user.id ,ctrl.user.type)
    # order_sender.SendOrder()

def initialization():
    # frame_request.pack_forget()
    # frame_stock_list.pack_forget()
    # label1.pack_forget()
    # btn_complete.pack_forget()
    list = root.pack_slaves()
    for pack in list:
        pack.pack_forget()
    btn_s.pack()
    btn_wh.pack()
def printResult():
    btn_order_request.pack_forget()
    btn_order_result_check.pack_forget()
    frame_result.pack(fill='both',expand=True)
    btn_complete.pack(side='bottom')

def CheckOrder():
    mode = 'off'
    if mode == 'on':
        list = root.pack_slaves()
        for pack in list:
            pack.pack_forget()
        frame_auto_result.pack(fill='both',expand=True)
        btn_complete.pack(side='bottom')
    else:
        list = root.pack_slaves()
        for pack in list:
            pack.pack_forget()
        frame_self_result.pack()
        Button(frame_self_result, width = 15, height = 1, text= 'Reject').pack(side='bottom')
        Button(frame_self_result, width = 15, height = 1, text= 'Accept').pack(side='bottom')
        btn_complete.pack(side='bottom')
btn_s = Button(root, width = 10, height = 2,text = "점주", command=initiate_s)
btn_wh = Button(root, width = 10, height = 2, text = "창고주", command=initiate_wh)

btn_order_request = Button(root, width = 15, height= 2, text = "발주 신청", command=MakeOrder)
btn_order_result_check = Button(root, width= 15, height=2,text = "발주 결과 확인",command = printResult)

btn_order_check = Button(root, width = 15, height= 2, text = "발주 확인", command=CheckOrder)
btn_exit = Button(root, width = 15, height= 2, text = "종료", command=root.destroy)


frame_stock_list = LabelFrame(root, text= "연결된 창고 stock_list")
# frame_stock_list.pack(side="left",expand=True)
frame_request = LabelFrame(root, text= "주문 신청")

label1= Label(root, text="주문 목록 생성")
btn_complete = Button(root, text="완료",command = initialization)

frame_result = LabelFrame(root, text= "발주 결과")
Label(frame_result, text= "{:^20} : {:^20}".format("order_number","result")).pack()
Label(frame_result, text= "{:^20} : {:^20}".format("w202105275313323","Accept")).pack()
Label(frame_result, text= "{:^20} : {:^20}".format("w202105275313335","Reject")).pack()
Label(frame_result, text= "{:^20} : {:^20}".format("w202105275313355","Ready")).pack()

frame_auto_result = LabelFrame(root, text= "auto_order_result")
Label(frame_auto_result, text= "{:^20} : {:^20}".format("order_number","result")).pack()
Label(frame_auto_result, text= "{:^20} : {:^20}".format("w202105275313323","Accept")).pack()
Label(frame_auto_result, text= "{:^20} : {:^20}".format("w202105275313335","Reject")).pack()
Label(frame_auto_result, text= "{:^20} : {:^20}".format("w202105275313355","Ready")).pack()

frame_self_result = LabelFrame(root, text= "self_order_result")
Label(frame_self_result, text= "{:^50} : {:^20}".format("name brand price num","stock #")).pack()
Label(frame_self_result, text= "{:^50} : {:^20}".format("beer kloud 1500 200","1200")).pack()
Label(frame_self_result, text= "{:^50} : {:^20}".format("milk seoul 600 400","1500")).pack()


btn_s.pack()
btn_wh.pack()

root.mainloop()


