import OrderList
import MoneyChecker as mc
import os
class OrderSender: # 발주를 보내면 주문번호.txt생성
    def __init__(self, order, user_id):
        self.order = order
        self.user_id = user_id

    def SendOrder(self): # 신청 시 Ready 상태로 파일 생성.
        if mc.MoneyChecker(self.order.total_price).checkBalance(): # 잔고 확인 후 잔고가 충분하면 Send
            if os.path.isdir(os.getcwd() + '\\' + self.user_id + "_Order") == False:
                os.mkdir(os.getcwd() + '\\' + self.user_id + "_Order")
            order_file = open(os.getcwd() + '\\' + self.user_id + "_Order\\" + self.order.order_number + ".txt", "w", encoding="utf8")
            print("{}".format("Ready"), file = order_file)
            for i in range(len(self.order.item_name)):
                print("{} {} {} {}".format(self.order.item_name[i], self.order.item_brand[i], self.order.item_price[i], self.order.item_number[i]), file = order_file)
            order_file.close()
        else:
            print("돈이 부족해서 발주 신청이 취소되었습니다.")