import OrderListMaker

class OrderSender:
    def __init__(self, order_num, order_list, wh, user_id):
        self.order_list = order_list
        self.order_num = order_num
        self.receiver = wh
        self.sender = user_id

    def SendOrder(self):
        order_file = open(self.receiver + "\\" + self.order_num + ".txt", "w", encoding="utf8")

