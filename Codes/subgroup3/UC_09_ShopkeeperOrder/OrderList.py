class OrderList:
    def __init__(self,item_name,item_brand, item_price, item_number, order_number):
        self.item_name = item_name
        self.item_brand = item_brand
        self.item_price = item_price
        self.item_number = item_number
        self.total_price = 0
        self.order_number = order_number
        self.length = len(self.item_name)
        for i in range(len(item_price)):
            self.total_price += item_price[i]*item_number[i]
        
    def printOrderList(self):
        if self.item_price == []:
            self.item_price = [0 for i in range(self.length)]
        print("OrderList>>.>>>>>")
        for i in range(self.length):
            print("{0: <20}{1: <20}{2: <20}{3: <20}".format(self.item_name[i],self.item_brand[i],self.item_price[i],self.item_number[i]))

