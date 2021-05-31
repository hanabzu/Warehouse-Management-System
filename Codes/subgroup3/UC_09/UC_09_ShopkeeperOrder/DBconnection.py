from . import OrderList

class DBconnection:
    def __init__(self, result, order_list):
        self.result = result
        self.order_list = order_list

    def UpdateStock(self):
        stock_file = open("stock_list.txt", "r", encoding="utf8")
        item_name = []
        item_brand = []
        item_price = []
        item_number = []
        while True:
            line = stock_file.readline()
            if not line:  # line이 없으면, 읽어올 라인이 없으면
                break
            temp = line.split(' ')
            item_name.append(temp[0])
            item_brand.append(temp[1])
            item_price.append((int)(temp[2]))
            item_number.append((int)(temp[3]))

        stock_file.close()

        stock_name_brand = []
        for i in range(len(item_name)): # name, brand로 아이템을 구분 하므로 찾기 편하게 묶어서 list만들기.
            stock_name_brand.append((item_name[i],item_brand[i]))

        stock_file = open("stock_list.txt", "w", encoding="utf8")
        iter = 0
        for order in self.order_list:
            if self.result[iter] == 'Accept':  ## 결과가 Accept일때만 재고 감소
                for i in range(len(order.item_name)):
                    stock_index = stock_name_brand.index((order.item_name[i], order.item_brand[i])) # 재고 데이터 인덱스 찾기.
                    item_number[stock_index] -= order.item_number[i]
            iter += 1

        for i in range(len(item_name)):
            print("{} {} {} {}".format(item_name[i],item_brand[i], item_price[i], item_number[i]), file= stock_file)
        stock_file.close()

        
        
