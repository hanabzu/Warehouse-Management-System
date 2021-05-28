import OrderSender as ods

class OrderList:
    def __init__(self,item_name,item_brand, item_price, item_number):
        self.item_name = item_name
        self.item_brand = item_brand
        self.item_price = item_price
        self.item_number = item_number
        self.total_price = 0
        self.length = len(self.item_name)
        for i in range(len(item_price)):
            self.total_price += item_price[i]*item_number[i]
        
    def printOrderList(self):
        print("OrderList>>.>>>>>")
        for i in range(self.length):
            print("{0: <20}{1: <20}{2: <20}{3: <20}".format(self.item_name[i],self.item_brand[i],self.item_price[i],self.item_number[i]))


class OrderListMaker:
    def __init__(self, connected_wh):
        self.warehouse = connected_wh
        self.total_price = 0
        self.OrderList = None
        self.item_name = []
        self.item_brand = []
        self.item_price = []
        self.item_number = []

        self.view_stock()
        self.MakeOrder()
    #stub

    def getPrice(self):
        return self.total_price

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

    def re_veiw_stock(self): # 파일에서 읽어온 stock info를 print
        print("{0: <20}{1: <20}{2: <20}{3: <20}".format("name", "brand", "price", "number"))
        for i in range(len(self.item_name)):
            print("{0: <20}{1: <20}{2: <20}{3: <20}".format(self.item_name[i],self.item_brand[i],self.item_price[i],self.item_number[i]))

    def MakeOrder(self):
        temp_name = []
        temp_brand = []
        temp_price = []
        temp_number = []
        while True:
            self.re_veiw_stock()
            print("if you choose all item type 'stop'")
            choice = input("Choose item. (name brand number) : ")
            if choice == "stop":
                break
            temp = choice.split(' ')
            if self.check_stock(temp[0], temp[1],(int)(temp[2])):
                temp_name.append(temp[0])
                temp_brand.append(temp[1])
                temp_price.append(self.check_price(temp[0],temp[1]))
                temp_number.append((int)(temp[2]))
            else:
                print("invalid input : Out of stock!")

        self.OrderList = OrderList(temp_name,temp_brand, temp_price, temp_number)
        self.total_price = self.OrderList.total_price

    def check_stock(self, name, brand, number):
        for i in range(len(self.item_name)):
            if self.item_name[i] == name and self.item_brand[i] == brand:
                if self.item_number[i] < number:
                    return False
                else:
                    return True
        return False # 해당 재고 없음

    def check_price(self, name, brand):
        for i in range(len(self.item_name)):
            if self.item_name[i] == name and self.item_brand[i] == brand:
                return self.item_price[i]
        return 0 # 해당 상품 없을 때
        
    def OrderNumberMaker(self):
        
            