import os

class DBconnection:
    def __init__(self, user_id):
        self.user_id = user_id

    def EditStock(self):
        item_name = []
        item_brand = []
        item_price = []
        item_number = []
        # 신청한 발주 목록 확인해서 받아오기.
        if os.path.isdir(os.getcwd() + '\\' + self.user_id + "_Order") == False:
            print("주문 신청한 목록이 없습니다.")
        order_file = os.listdir(os.getcwd() + '\\' + self.user_id + "_Order") # 주문은 한번 발송. 2개 이상 쌓여있지 않다.
        file = open(os.getcwd() + '\\' + self.user_id + "_Order\\" + order_file[0], 'r', encoding='utf8')
        lines = file.readlines()
        for line in lines[1:]:
            temp = line.rstrip('\n').split(' ')
            item_name.append(temp[0])
            item_brand.append(temp[1])
            item_price.append(int(temp[2]))
            item_number.append(int(temp[3]))
        file.close()
        # stock_list(Db) update
        # stock_list 정보 가져오기.
        stock_name_brand, stock_item_price, stock_item_number = self.stock_check()
        for i in range(len(item_name)):
            if stock_name_brand.count((item_name[i],item_brand[i])) == 0: # 재고목록에 없는 아이템 발주신청했을 때
                stock_name_brand.append((item_name[i],item_brand[i]))
                stock_item_price.append(item_price[i])
                stock_item_number.append(item_number[i])
            else: #재고 목록에 있을 때는 + 해준다.
                index = stock_name_brand.index((item_name[i],item_brand[i]))
                stock_item_number[index] += item_number[i]
        file = open("stock_list.txt", 'w', encoding='utf8')
        for i in range(len(stock_name_brand)):
            print("{} {} {} {}".format(stock_name_brand[i][0],stock_name_brand[i][1], stock_item_price[i], stock_item_number[i]), file= file)
        file.close()
        # 발주 신청 성공했으면 읽은 파일은 삭제. 
        if os.path.isfile(os.getcwd() + '\\' + self.user_id + "_Order\\" + order_file[0]):
                os.remove(os.getcwd() + '\\' + self.user_id + "_Order\\" + order_file[0])
        else:
            print("{} is not exist".format(os.getcwd() + '\\' + self.user_id + "_Order\\" + order_file[0]))
            
    def clear_order_list(self):
        order_file = os.listdir(os.getcwd() + '\\' + self.user_id + "_Order") 
        if os.path.isfile(os.getcwd() + '\\' + self.user_id + "_Order\\" + order_file[0]):
                os.remove(os.getcwd() + '\\' + self.user_id + "_Order\\" + order_file[0])
        else:
            print("{} is not exist".format(os.getcwd() + '\\' + self.user_id + "_Order\\" + order_file[0]))

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