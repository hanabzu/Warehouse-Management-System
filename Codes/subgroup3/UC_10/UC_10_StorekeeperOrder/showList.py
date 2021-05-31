import OrderList

class showList:
    def __init__(self, orderList):
        self.orderList = orderList
        self.showList()
    def showList(self):
        print("생성된 발주 목록 : ")
        self.orderList.printOrderList()
    


