import OrderList
import datetime
class OrderMaker:
    def __init__(self, user_id):
        self.user_id = user_id

    def MakeOrder(self):
        #주문 목록
        order_item_name = []
        order_item_brand = []
        order_item_price =[]
        order_item_number = []
        order_number = self.OrderNumberMaker()


        # 재고 상황 확인
        stock_name_brand, stock_item_price ,stock_item_number = self.stock_check()
        # 예측 판매량 확인
        pred_name_brand, pred_item_number = self.pred_check()
        # 구매 가능한 생산품 확인        
        product_name_brand, product_item_price = self.production_check()

        # 주문 수량 파익 및 발주 목록 생성
        for i in range(len(pred_name_brand)):
            if stock_name_brand.count(pred_name_brand[i]) == 0: # 예측 판매량 상품이 재고에 존재하지 않을 때 - 예측 판매량 그대로 주문 목록에 추가.
                if product_name_brand.count(pred_name_brand[i]) != 0: # 구매 가능한 생산품이면.
                    order_item_name.append(pred_name_brand[i][0])
                    order_item_brand.append(pred_name_brand[i][1])
                    temp_index = product_name_brand.index(pred_name_brand[i]) # 가격은 product_list에서 확인.
                    order_item_price.append(product_item_price[temp_index])
                    order_item_number.append(pred_item_number[i])
            else: #예측 판매량 상품이 존재할 때
                if product_name_brand.count(pred_name_brand[i]) != 0: #구매 가능한 생산품이면.
                    stock_index = stock_name_brand.index(pred_name_brand[i]) # 해당 상품 인덱스 찾고
                    order_Quantity = pred_item_number[i] - stock_item_number[stock_index] # 주문 수량은 (예측량 - 재고량)
                    order_item_name.append(pred_name_brand[i][0])
                    order_item_brand.append(pred_name_brand[i][1])
                    order_item_price.append(stock_item_price[stock_index]) # 가격은 재고목록에 있는 것을 사용
                    order_item_number.append(order_Quantity)

        return OrderList.OrderList(order_item_name, order_item_brand, order_item_price, order_item_number, order_number) #OrderList객체로 반환

    def Passive_MakeOrder(self):
        temp_name = []
        temp_brand = []
        temp_price = []
        temp_number = []
        # 구매 가능한 생산품 확인        
        product_name_brand, product_item_price = self.production_check()
        while True:
            self.view_productList(product_name_brand, product_item_price)
            print("if you choose all item type 'stop'")
            choice = input("Choose item. (name brand number) : ")
            if choice == "stop":
                break
            temp = choice.split(' ')
            if self.check_product(temp[0], temp[1],product_name_brand):
                temp_name.append(temp[0])
                temp_brand.append(temp[1])
                temp_price.append(self.check_price(temp[0],temp[1],product_name_brand, product_item_price))
                temp_number.append((int)(temp[2]))
            else:
                print("invalid input : Out of stock!")

        return OrderList.OrderList(temp_name,temp_brand, temp_price, temp_number, self.OrderNumberMaker())

    def view_productList(self, product_name_brand, product_item_price):
        for i in range(len(product_name_brand)):
            print("{:<20}|{:<20}|{:<20}".format(product_name_brand[i][0],product_name_brand[i][1], product_item_price[i]))

    def check_product(self, name, brand,product_name_brand):
        if product_name_brand.count((name,brand)) != 0:
            return True
        return False # 해당 생산품 없음

    def check_price(self, name, brand,product_name_brand, product_item_price):
        if product_name_brand.count((name,brand)) != 0:
            return product_item_price[product_name_brand.index((name,brand))]
        return 0 # 해당 상품 없을 때           


    def stock_check(self):
        # 재고 상황 확인
        stock_item_name = []
        stock_item_brand = []
        stock_item_price = []
        stock_item_number = []
        stock_file = open("stock_list.txt", "r", encoding="utf8")        
        while True:
            line = stock_file.readline()
            if not line:  # line이 없으면, 읽어올 라인이 없으면
                break
            temp = line.split(' ') 
            stock_item_name.append(temp[0])
            stock_item_brand.append(temp[1])
            stock_item_price.append(int(temp[2]))
            stock_item_number.append((int)(temp[3]))
        stock_file.close()
        stock_name_brand = []
        for i in range(len(stock_item_name)): # name, brand로 아이템을 구분 하므로 찾기 편하게 묶어서 list만들기.
            stock_name_brand.append((stock_item_name[i],stock_item_brand[i]))

        return stock_name_brand, stock_item_price, stock_item_number 
    
    def pred_check(self):
        #예측 판매량 확인
        pred_item_name = []
        pred_item_brand = []
        pred_item_number = []
        pred_file = open("prediction.txt", "r", encoding="utf8")        
        while True:
            line = pred_file.readline()
            if not line:  # line이 없으면, 읽어올 라인이 없으면
                break
            temp = line.split(' ') 
            pred_item_name.append(temp[0])
            pred_item_brand.append(temp[1])
            pred_item_number.append(int(temp[2]))
        pred_file.close()
        pred_name_brand = []
        for i in range(len(pred_item_name)): # name, brand로 아이템을 구분 하므로 찾기 편하게 묶어서 list만들기.
            pred_name_brand.append((pred_item_name[i],pred_item_brand[i]))

        return pred_name_brand, pred_item_number 

    def production_check(self):
        #생산품 확인
        production_item_name = []
        production_item_brand = []
        production_item_price = []
        production_file = open("product_list.txt", "r", encoding="utf8")        
        while True:
            line = production_file.readline()
            if not line:  # line이 없으면, 읽어올 라인이 없으면
                break
            temp = line.split(' ') 
            production_item_name.append(temp[0])
            production_item_brand.append(temp[1])
            production_item_price.append(int(temp[2]))
        production_file.close()
        production_name_brand = []
        for i in range(len(production_item_name)): # name, brand로 아이템을 구분 하므로 찾기 편하게 묶어서 list만들기.
            production_name_brand.append((production_item_name[i],production_item_brand[i]))

        return production_name_brand, production_item_price 

    #주문 번호 생성
    def OrderNumberMaker(self):
        date = datetime.datetime.now()
        order_num = self.user_id + "{0}{1}{2}{3}".format(date.month, date.day, date.minute , date.second)
        return order_num