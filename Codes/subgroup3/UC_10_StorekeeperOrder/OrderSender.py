import OrderList

class OrderSender: # 발주를 보내면 주문번호.txt생성
    def __init__(self, order):
        self.order = order

    def SendOrder(self): # 신청 시 Ready 상태로 파일 생성.
        order_file = open(self.order.order_number + ".txt", "w", encoding="utf8")
        print("{}".format("Ready"), file = order_file)
        for i in range(len(self.order_list.item_name)):
            print("{} {} {} {}".format(self.order_list.item_name[i], self.order_list.item_brand[i], self.order_list.item_price[i], self.order_list.item_number[i]), file = order_file)
        order_file.close()
