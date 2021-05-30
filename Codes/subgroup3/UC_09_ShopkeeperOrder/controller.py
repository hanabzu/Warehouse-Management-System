import OrderListMaker as olm
import OrderSender as ods
import OrderAccepter as oa
import DBconnection as db
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
        
        if self.user.type == 'shop':
            order_list = self.MakeOrder()
            order_sender = ods.OrderSender(order_list, self.user.connected, self.user.id ,self,user.type)
            order_sender.SendOrder()

            # 결과확인 시
            # ResultSender모듈을 통해서 결과 확인.
            # 결과 확인 후 MOneyChanger로 money 차감.
        else:
            receive_order_list, sender_list = self.TakeOrder()
            if len(receive_order_list) != 0:
                order_accepter = oa.OrderAccepter(self.user.id, receive_order_list)
                if self.user.mode == 'on':
                    order_accepter.AutoChecker()
                else:
                    order_accepter.selfcheck()
                Result = order_accepter.getResult() # Accept/ Reject 결과 리스트 반환 받기.

                for i in range(len(Result)):
                    pass
                    #DB connection 으로 재고에 반영

                #Result Sender로 결과 전송

                #

    def TakeOrder(self):
        order_taker = ods.OrderTaker(self.user.id)
        receive_order_list, sender_list = order_taker.TakeOrder()
        return receive_order_list, sender_list

    def MakeOrder(self):
        OrderListMaker = olm.OrderListMaker("w20210527")
        self.price = OrderListMaker.getPrice()
        return OrderListMaker.OrderList


#driver
class initiator:
    def __init__(self):
        user_type = input("1. 창고주 / 2. 점주 ")
        user_info = []
        if user_type == 1:
            user_info.append("warehouse")
            info_file = open("창고주.txt", "r", encoding="utf8")
            for i in range(4):
                line = info_file.readline()
                temp = line.split(' ')
                user_info.append(temp[2][:-1])
            now_user = wh_user(user_info[0],user_info[1],user_info[2],user_info[3], user_info[4])
        else:
            user_info.append("shop")
            info_file = open("점주.txt", "r", encoding="utf8")
            for i in range(3):
                line = info_file.readline()
                temp = line.split(' ')
                user_info.append(temp[2][:-1])
            now_user = sh_user(user_info[0],user_info[1],user_info[2],user_info[3])
        
        controller(now_user)


# initiator()
# user_info = []
# info_file = open("창고주.txt", "r", encoding="utf8")
# user_info.append("warehouse")
# for i in range(4):
#     line = info_file.readline()
#     temp = line.split(' ')
#     user_info.append(temp[2][:-1])
# now_user = wh_user(user_info[0],user_info[1],user_info[2],user_info[3], user_info[4])

# print(now_user.connected, now_user.id, now_user.mode, now_user.money, now_user.type)