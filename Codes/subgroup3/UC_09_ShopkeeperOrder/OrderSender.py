import OrderListMaker
import OrderList
import os
class OrderSender:
    def __init__(self, order_list, receiver, user_id, user_type):
        self.order_list = order_list
        self.user_type = user_type
        if self.user_type == "shop": # 점주 일때는 sendOrder
            self.receiver = receiver
            self.sender = user_id

    def SendOrder(self):
        if os.path.isdir(os.getcwd() + '\\' + self.receiver + "_Order") == False:
            os.mkdir(os.getcwd() + '\\' + self.receiver + "_Order")

        order_file = open(self.receiver + "_Order" + "\\" + self.order_list.order_number + ".txt", "w", encoding="utf8")
        print("{}".format(self.sender), file = order_file)
        for i in range(len(self.order_list.item_name)):
            print("{} {} {} {}".format(self.order_list.item_name[i], self.order_list.item_brand[i], self.order_list.item_price[i], self.order_list.item_number[i]), file = order_file)
        order_file.close()
        if os.path.isdir(os.getcwd() + '\\' + self.sender + "_Order") == False:
            os.mkdir(os.getcwd() + '\\' + self.sender + "_Order")
        order_file2 = open(self.sender + "_Order" +  "\\" + self.order_list.order_number + ".txt", "w", encoding="utf8")
        print("Ready", file= order_file2)
        for i in range(len(self.order_list.item_name)):
            print("{} {} {} {}".format(self.order_list.item_name[i], self.order_list.item_brand[i], self.order_list.item_price[i], self.order_list.item_number[i]), file = order_file2)
        order_file2.close()

class OrderTaker:
    def __init__(self,user_id):
        self.user_id = user_id
    def TakeOrder(self): # return Receive_Order, sender_list
        Receive_Orders = []
        temp_name = []
        temp_brand = []
        temp_price = []
        temp_number = []
        if os.path.isdir(os.getcwd() + '\\' + self.user_id + "_Order"):
            order_list = os.listdir(self.user_id + "_Order")
        else:
            order_list = []
        sender_list = []
        if len(order_list) == 0:
            print("No receive order!")
            pass
        else:
            for i in range(len(order_list)):
                file = open(self.user_id + "_Order\\" + order_list[i], "r", encoding="utf8")
                temp = file.readline()
                sender_list.append(temp.rstrip('\n'))
                while True:
                    line = file.readline()
                    if not line:  # line이 없으면, 읽어올 라인이 없으면
                        break
                    temp = line.split(' ')
                    temp_name.append(temp[0])
                    temp_brand.append(temp[1])
                    temp_price.append(int(temp[2]))
                    temp_number.append(int(temp[3]))
                Receive_Orders.append(OrderList.OrderList(temp_name[:],temp_brand[:],[],temp_number[:], order_list[i][:-4]))
                temp_name.clear()
                temp_brand.clear()
                temp_price.clear()
                temp_number.clear()
                file.close()
        return Receive_Orders, sender_list

