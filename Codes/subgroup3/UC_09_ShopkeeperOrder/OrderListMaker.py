class OrderList:
    def __init__(self,item_name,item_brand, item_price, item_number):
        self.item_name = item_name
        self.item_brand = item_brand
        self.item_price = item_price
        self.item_number = item_number
        self.total_price = 0
        for i in range(len(item_price)):
            self.total_price += item_price[i]*item_number[i]
        

class OrderListMaker:
    def __init__(self, connected_wh):
        self.warehouse = connected_wh
        self.total_price = 0
        self.OrderList = None
        self.item_name = []
        self.item_brand = []
        self.item_price = []
        self.item_number = []
    #stub
    def view_stock(self):
        stock_file = open("stock_list.txt", "r", encoding="utf8")
        
        while True:
            line = stock_file.readline()
            if not line:  # line이 없으면, 읽어올 라인이 없으면
                break
            temp = line.split(' ')
            self.item_name.append(temp[0])
            self.item_brand.append(temp[1])
            self.item_price.append((int)(temp[2]))
            self.item_number.append((int)(temp[3]))

        print("{0: <20}{1: <20}{2: <20}{3: <20}".format("name", "brand", "price", "number"))
        for i in range(len(self.item_name)):
            print("{0: <20}{1: <20}{2: <20}{3: <20}".format(self.item_name[i],self.item_brand[i],self.item_price[i],self.item_number[i]))
        stock_file.close()

    def MakeOrder(self):
        pass



test = OrderListMaker("w20210527")

test.view_stock()
    
