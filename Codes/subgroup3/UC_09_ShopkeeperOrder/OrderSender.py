import OrderListMaker
import os
class OrderSender:
    def __init__(self, order_num, order_list, receiver, user_id, user_type):
        self.order_list = order_list
        self.order_num = order_num
        self.user_type = user_type
        if self.user_type == "shop": # 점주 일때는 sendOrder
            self.receiver = receiver
            self.sender = user_id
        else:                        # 창고주 일때는 TakeOrder
            self.sender = receiver
            self.receiver = user_id

    def SendOrder(self):
        order_file = open(self.receiver + "_Order" + "\\" + self.order_num + ".txt", "w", encoding="utf8")
        print("{}".format(self.sender), file = order_file)
        for i in range(len(self.order_list.item_name)):
            print("{} {} {}".format(self.order_list.item_name[i], self.order_list.item_brand[i], self.order_list.item_number[i]), file = order_file)
        order_file.close()

        order_file2 = open(self.sender + "_Order" +  "\\" + self.order_num + ".txt", "w", encoding="utf8")
        print("Ready", file= order_file2)
        for i in range(len(self.order_list.item_name)):
            print("{} {} {}".format(self.order_list.item_name[i], self.order_list.item_brand[i], self.order_list.item_number[i]), file = order_file)
        order_file2.close()
    
    def TakeOrder(self):
        Receive_Order = []
        temp_name = []
        temp_brand = []
        temp_number = []
        order_list = os.listdir(self.sender + "_Order")
        if len(order_list) == 0:
            pass
        else:
            for i in range(len(order_list)):
                file = open(order_list[i], "r", encoding="utf8")
                temp = file.split(' ')
                temp_name.append(temp[0])
                temp_brand.append(temp[1])
                temp_number.append((int)(temp[2]))
