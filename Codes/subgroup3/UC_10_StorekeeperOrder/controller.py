import OrderDate as od

class controller:
    def __init__(self):
        self.orderdate = self.createOrderDate()

        self.orderdate.printOD()
        choice = int(input("1. 발주 날짜 변경 2....."))

        if choice == 1:
            # 발주 날짜 변경 옵션 선택 시
            self.orderdate = self.EditOrderDate()
        

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
class initiator:
    def __init__(self):
        controller()

initiator()

