import OrderList

class OrderEditor:
    def __init__(self, order_list):
        self.order_list = order_list # 자동 모드 off일때는 None으로 들어와서 직접 만들 수 있도록.
        if order_list == None:
            print("make orderList first!")
            pass
        else:
            self.EditOrder()
    def EditOrder(self):
        # 구매 가능한 생산품 확인   
        order_name_brand = []
        for i in range(len(self.order_list.item_name)): # name, brand로 아이템을 구분 하므로 찾기 편하게 묶어서 list만들기.
            order_name_brand.append((self.order_list.item_name[i],self.order_list.item_brand[i]))

        product_name_brand, product_item_price = self.production_check()
        while True:
            print("현재 신청 발주 목록 : ")
            self.order_list.printOrderList()
            print("신청 가능한 생산품 목록 : ")
            self.view_productList(product_name_brand, product_item_price)
            print("if you choose all item type 'stop'")
            choice = input("Choose item. (name brand number) : ")
            if choice == 'stop':
                print("test!!!!!!!!!!!!!!!!!!!!!!")
                break
            temp = choice.split(' ')
            if self.check_product(temp[0], temp[1],product_name_brand): # 입력한 품목이 신청가능한 품목인지 확인하고
                if order_name_brand.count((temp[0],temp[1])) == 0: # 신청 발주목록에 입력한 품목이 없을 때
                    #발주 리스트에 해당 품목 추가.
                    self.order_list.item_name.append(temp[0])
                    self.order_list.item_brand.append(temp[1])
                    self.order_list.item_price.append(self.check_price(temp[0],temp[1],product_name_brand, product_item_price))
                    self.order_list.item_number.append(int(temp[2]))
                else: # 신청 발주목록에 입력한 품목이 있을 때
                    temp_index= order_name_brand.index((temp[0],temp[1])) # 발주목록의 인덱스를 찾아서
                    self.order_list.item_number[temp_index] = int(temp[2]) # 수정한 개수 반영.

            else:
                print("invalid input : No product!")

        return self.order_list

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

    def view_productList(self, product_name_brand, product_item_price):
        print("{:<20}|{:<20}|{:<20}".format("product_name","product_brand", "product_price"))
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

    
    


