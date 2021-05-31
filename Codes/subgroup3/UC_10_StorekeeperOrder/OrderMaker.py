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