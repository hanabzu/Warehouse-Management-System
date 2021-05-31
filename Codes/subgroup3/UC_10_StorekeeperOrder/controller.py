import OrderDate as od
import DateCounter as dc
import OrderMaker as om
import OrderList
import showList
class controller:
    def __init__(self, user):
        self.user = user
        self.orderdate = self.createOrderDate()
        self.isDay = dc.Datecounter(self.orderdate.date, self.orderdate.n_day).DateCheck()
        self.orderList = None
        while True:
            choice = int(input("1. 발주 날짜 변경 2.자동 발주 테스트 3.showList 테스트 4.수동 발주 테스트"))

            if choice == 1:
                # 발주 날짜 변경 옵션 선택 시
                self.orderdate = self.EditOrderDate()
                self.isDay = dc.Datecounter(self.orderdate.date, self.orderdate.n_day).DateCheck()
            elif choice == 2:
                self.orderList = om.OrderMaker(user.user_id).MakeOrder()
                self.orderList.printOrderList()
            elif choice == 3:
                showList.showList(self.orderList)
            elif choice == 4:
                self.orderList = om.OrderMaker(user.user_id).Passive_MakeOrder()
                self.orderList.printOrderList()
            else:
                break
        

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
        print(lines[3].rstrip('/n'), file= file)
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
                user_money = temp[-1]
            elif temp[0] == 'order_date':
                pass
            else:
                print(temp[0])
                print("error! 창고주.txt파일 점검 필요!")
        return user(user_id, user_mode, user_money)
            

initiator()

