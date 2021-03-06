import OrderDate as od
import DateCounter as dc
import OrderMaker as om
import OrderEditor as oe
import OrderSender as ods
import MessageSender as ms
import DBconnection as db
import OrderList
import showList
class controller:
    def __init__(self, user):
        self.user = user
        self.orderdate = self.createOrderDate()
        self.isDay = dc.Datecounter(self.orderdate.date, self.orderdate.n_day).DateCheck()
        self.orderList = None
        self.isOrderDay = dc.Datecounter(self.orderdate.date, self.orderdate.n_day).OrderDateCheck()
        # while True:
        #     choice = int(input("1. 발주 날짜 변경 2.자동 발주 테스트 3.showList 테스트 4.수동 발주 테스트 5.EditOrder Test, 6.SendOrder Test 7.Take Result Test\
        #         8.DBconnection Test"))

        #     if choice == 1:
        #         # 발주 날짜 변경 옵션 선택 시
        #         self.orderdate = self.EditOrderDate()
        #         self.isDay = dc.Datecounter(self.orderdate.date, self.orderdate.n_day).DateCheck()
        #     elif choice == 2:
        #         self.orderList = om.OrderMaker(user.user_id).MakeOrder()
        #         self.orderList.printOrderList()
        #     elif choice == 3:
        #         showList.showList(self.orderList)
        #     elif choice == 4:
        #         self.orderList = om.OrderMaker(user.user_id).Passive_MakeOrder()
        #         self.orderList.printOrderList()
        #     elif choice == 5:
        #         self.orderList = oe.OrderEditor(self.orderList).getOrderList()
        #         self.orderList.printOrderList()
        #     elif choice == 6:
        #         ods.OrderSender(self.orderList, self.user.user_id).SendOrder()
        #     elif choice == 7:
        #         ms.MessageSender(self.orderList.order_number, self.user.user_id).RejectOrder()
        #         print(ms.ResultTaker(self.user.user_id).TakeResult())
        #         ms.MessageSender(self.orderList.order_number, self.user.user_id).AcceptOrder()
        #         print(ms.ResultTaker(self.user.user_id).TakeResult())
        #     elif choice == 8:
        #         if ms.ResultTaker(self.user.user_id).TakeResult()[0] == 'Accept':
        #             db.DBconnection(self.user.user_id).EditStock()
        #     else:
        #         break
        choice = int(input("1.발주 날짜 변경 2. 발주 신청 목록 만들기."))
        if choice == 1:
            self.orderdate = self.EditOrderDate()
            self.isDay = dc.Datecounter(self.orderdate.date, self.orderdate.n_day).DateCheck()
        if user.user_mode == 'on': #자동 발주 신청 모드일때
            self.orderList = om.OrderMaker(user.user_id).MakeOrder() # 발주 리스트 생성.
            if choice == 2:
                showList.showList(self.orderList) #보여주기.
            if self.isDay: #발주 날짜 n일 전이면
                self.orderList = oe.OrderEditor(self.orderList).getOrderList()
            else:
                pass
        else:
            if choice == 2:
                self.orderList = om.OrderMaker(user.user_id).Passive_MakeOrder()

        if self.isOrderDay:# 발주 날짜면
            ods.OrderSender(self.orderList, self.user.user_id).SendOrder()
            ms.MessageSender(self.orderList.order_number, self.user.user_id).RejectOrder() # Reject stub
            result, order_number = ms.ResultTaker(self.user.user_id).TakeResult()
            # ms.MessageSender(self.orderList.order_number, self.user.user_id).AcceptOrder() # Accept stub
            # result, order_number =ms.ResultTaker(self.user.user_id).TakeResult()
            if result == 'Error':
                pass
            else:
                print("<발주 신청 결과>")
                print("{} : {}".format(order_number, result))
                if result == 'Accept': # 받은 결과가 Accept면
                    db.DBconnection(self.user.user_id).EditStock()
                if result == 'Reject':
                    db.DBconnection(self.user.user_id).clear_order_list()


        

    def createOrderDate(self):
        file = open("창고주.txt", 'r',  encoding='utf8')
        lines = file.readlines()
        for line in lines:
            temp = line.split(' ')
            if temp[0] == 'order_date':
                order_date = int(temp[2])
                order_n_day = int(temp[3])
                break
        file.close()
        return od.OrderDate(order_date, order_n_day)

    def EditOrderDate(self):
        file = open("창고주.txt", 'r',  encoding='utf8')
        lines = file.readlines()
        file.close()
        order_date = int(input("발주 날짜(일) : "))
        order_n_day = int(input("발주 생성일(n일전) : "))
        file = open("창고주.txt", 'w', encoding= 'utf8')
        print(lines[0].rstrip('\n'),file = file)
        print(lines[1].rstrip('\n'), file = file)
        print("order_date : {} {}".format(order_date, order_n_day), file = file)
        print(lines[3].rstrip('\n'), file= file)
        file.close()
        return od.OrderDate(order_date, order_n_day)

class user:
    def __init__(self, user_id, user_mode, user_money):
        self.user_id = user_id
        self.user_mode = user_mode
        self.user_money = user_money

class initiator:
    def __init__(self):
        controller(self.getUser_info())

    def getUser_info(self):
        file = open("창고주.txt", 'r',  encoding='utf8')
        lines = file.readlines()
        file.close()
        for line in lines:
            temp = line.rstrip('\n').split(' ')
            if temp[0] == 'id':
                user_id = temp[-1] 
            elif temp[0] == 'auto_mode':
                user_mode = temp[-1]
            elif temp[0] == 'money':
                user_money = int(temp[-1])
            elif temp[0] == 'order_date':
                pass
            else:
                print(temp[0])
                print("error! 창고주.txt파일 점검 필요!")
        return user(user_id, user_mode, user_money)
            

initiator()

