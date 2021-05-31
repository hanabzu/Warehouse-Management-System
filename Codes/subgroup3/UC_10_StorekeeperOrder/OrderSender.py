import OrderList
import MoneyChecker as mc
class OrderSender: # 발주를 보내면 주문번호.txt생성
    def __init__(self, order):
        self.order = order

    def SendOrder(self): # 신청 시 Ready 상태로 파일 생성.
        if mc.MoneyChecker(self.order.total_price).checkBalance(): # 잔고 확인 후 잔고가 충분하면 Send
            order_file = open(self.order.order_number + ".txt", "w", encoding="utf8")
            print("{}".format("Ready"), file = order_file)
            for i in range(len(self.order.item_name)):
                print("{} {} {} {}".format(self.order.item_name[i], self.order.item_brand[i], self.order.item_price[i], self.order.item_number[i]), file = order_file)
            order_file.close()
        else:
            print("돈이 부족해서 발주 신청이 취소되었습니다.")