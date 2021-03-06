from . import OrderListMaker as olm
from . import OrderSender as ods
from . import OrderAccepter as oa
from . import DBconnection as db
from . import ResultSender as rs
from . import MoneyChanger as mc
class sh_user:
    def __init__(self, type,id, connected,money):
        self.id = id
        self.type = type
        self.connected = connected
        self.money = money

class wh_user:
    def __init__(self, type,id, connected,money,auto_mode = 'on'):
        self.id = id
        self.type = type
        self.connected = connected
        self.money = money
        self.mode = auto_mode


class controller:
    def __init__(self, user):
        self.user = user
        self.price = 0
        self.result = None
        ### cli mode 시 ###
        if self.user.type == 'shop':
            choice = int(input("1.발주 신청  2. 발주 결과 확인 "))

            if choice == 1:
                # 발주 신청시
                order_list = self.MakeOrder()
                order_sender = ods.OrderSender(order_list, self.user.connected, self.user.id ,self.user.type)
                order_sender.SendOrder()
            else:
                # 결과확인 시
                # ResultSender모듈을 통해서 결과 확인.
                order_list, result = rs.ResultTaker(user.id).takeResult()
                for i in range(len(order_list)):
                    print(order_list[i].order_number, result[i])
                # 결과 확인 후 MOneyChanger로 money 차감.
                mc.MoneyChanger([order_list[i].total_price for i in range(len(order_list))],result,user.id).changeMoney()

        else:
            # 발주 확인 작동 가정
            choice = int(input("1.발주 확인 2. 종료"))
            if choice == 1:
                receive_order_list, sender_list = self.TakeOrder()
                if len(receive_order_list) != 0: # 받은 발주가 있을 때
                    order_accepter = oa.OrderAccepter(self.user.id, receive_order_list)

                    #자동 모드에 따라 발주 확인 및 승인/거절
                    if self.user.mode == 'on':
                        order_accepter.AutoChecker()
                    else:
                        order_accepter.selfcheck()
                    Result = order_accepter.getResult() # Accept/ Reject 결과 리스트 반환 받기.

                    db.DBconnection(Result, receive_order_list).UpdateStock() # 발주 승인에 따른 재고량 감소.
                    
                    # 결과 전송
                    rs.ResultSender(sender_list, Result, [receive_order_list[i].order_number for i in range(len(receive_order_list))]).sendResult()
                else:
                    print("종료합니다.")


    def TakeOrder(self):
        order_taker = ods.OrderTaker(self.user.id)
        receive_order_list, sender_list = order_taker.TakeOrder()
        return receive_order_list, sender_list

    def MakeOrder(self):
        OrderListMaker = olm.OrderListMaker(self.user.connected)
        self.price = OrderListMaker.getPrice()
        return OrderListMaker.OrderList


#driver
class initiator:
    def __init__(self,user_type):
        user_type = int(input("1. 창고주 / 2. 점주 "))
        user_info = []
        if user_type == 1:
            user_info.append("warehouse")
            info_file = open("창고주.txt", "r", encoding="utf8")
            for i in range(4):
                line = info_file.readline()
                temp = line.split(' ')
                user_info.append(temp[2].rstrip('\n'))
            now_user = wh_user(user_info[0],user_info[1],user_info[2],user_info[3], user_info[4])
        else:
            user_info.append("shop")
            info_file = open("점주.txt", "r", encoding="utf8")
            for i in range(3):
                line = info_file.readline()
                temp = line.split(' ')
                user_info.append(temp[2].rstrip('\n'))
            now_user = sh_user(user_info[0],user_info[1],user_info[2],user_info[3])
        self.now_user = now_user
        controller(self.now_user)
    def return_controller(self):
        return controller(self.now_user)


# initiator()
# user_info = []
# info_file = open("창고주.txt", "r", encoding="utf8")
# user_info.append("warehouse")
# for i in range(4):
#     line = info_file.readline()
#     temp = line.split(' ')
#     user_info.append(temp[2].rstrip('\n'))
# now_user = wh_user(user_info[0],user_info[1],user_info[2],user_info[3], user_info[4])

# print(now_user.connected, now_user.id, now_user.mode, now_user.money, now_user.type)