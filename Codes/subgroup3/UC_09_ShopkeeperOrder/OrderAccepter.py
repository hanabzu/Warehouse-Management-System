import OrderList
import os

class OrderAccepter:
    def __init__(self, user_id,order_list): # 모든 발주 목록에 대해 Accept/Reject 반환.
        self.user_id = user_id
        self.order_list = order_list[:] # copy해서 넣어준다.
        self.Result = []

    def getResult(self):
        return self.Result


    def AutoChecker(self):
        # 재고 상황 확인
        stock_item_name = []
        stock_item_brand = []
        stock_item_number = []
        stock_file = open("stock_list.txt", "r", encoding="utf8")        
        while True:
            line = stock_file.readline()
            if not line:  # line이 없으면, 읽어올 라인이 없으면
                break
            # price는 필요 x
            temp = line.split(' ') 
            stock_item_name.append(temp[0])
            stock_item_brand.append(temp[1])
            stock_item_number.append((int)(temp[3]))

        stock_name_brand = []
        for i in range(len(stock_item_name)): # name, brand로 아이템을 구분 하므로 찾기 편하게 묶어서 list만들기.
            stock_name_brand.append((stock_item_name[i],stock_item_brand[i]))


        for i in range(len(self.order_list)): # 모든 발주 목록에 대해 반복.
            temp_minus = []
            count = 0
            for j in range(len(self.order_list[i].item_name)): # 각 발주 목록의의 품목 개수에 대해 반복.
                if stock_name_brand.count(self.order_list[i].item_name[j], self.order_list[i].item_brand[j]) != 0: 
                    stock_index = stock_name_brand.index(self.order_list[i].item_name[j], self.order_list[i].item_brand[j]) # 재고 데이터 인덱스 찾기.
                    if stock_item_number[stock_index] < self.order_list[i].item_number[j]: #재고 보다 주문 수량이 많을 시
                        self.Result.append('Reject') #Reject하고 넘어감
                        break
                    else: #재고 보다 주문 수량이 적거나 같을 시
                        count += 1
                        temp_minus.append((stock_index, self.order_list[i].item_number[j] )) # Accept시 재고에서 빼주기 위해서 temp_minus에 index와 수량 저장
                else: # 해당 상품이 없으면 바로 Reject.
                    self.Result.append('Reject')
                    break
            if count == len(self.order_list[i].item_name): # 모든 발주 품목에 대해 재고 충분할 때
                self.Result.append('Accept')
                for i, number in temp_minus: # 저장해 둔 빼아할 수량을 Accept결정나고 빼준다.
                    stock_item_number[i] -= number

        for i in range(len(self.order_list)): # 모든 발주 목록에 대해 반복. Accept/Reject 결정 후 파일 삭제.
            order_file = self.user_id + "_Order\\" + self.order_list[i].order_number + ".txt"
            if os.path.isfile(order_file):
                os.remove(order_file)
            else:
                print("{} is not exist".format(order_file))
            

    def selfcheck(self):
        # 재고 상황 확인
        stock_item_name = []
        stock_item_brand = []
        stock_item_number = []
        stock_file = open("stock_list.txt", "r", encoding="utf8")        
        while True:
            line = stock_file.readline()
            if not line:  # line이 없으면, 읽어올 라인이 없으면
                break
            # price는 필요 x
            temp = line.split(' ') 
            stock_item_name.append(temp[0])
            stock_item_brand.append(temp[1])
            stock_item_number.append((int)(temp[3]))

        stock_name_brand = []
        for i in range(len(stock_item_name)): # name, brand로 아이템을 구분 하므로 찾기 편하게 묶어서 list만들기.
            stock_name_brand.append((stock_item_name[i],stock_item_brand[i]))
    
        for i in range(len(self.order_list)):
            ## 받은 발주 목록 보여주기
            self.showOrderList()        

            stock_index_list = [] # 해당 발주 목록 품목들의 재고 인덱스 리스트
            for j in range(len(self.order_list[i].item_name)):
                stock_index = stock_name_brand.index(self.order_list[i].item_name[j], self.order_list[i].item_brand[j]) # 재고 데이터 인덱스 찾기.
                stock_index_list.append(stock_index)
            
            ## 선택한 발주 품목, 재고상황 보여주기
            self.showOrder(i, stock_index_list, stock_item_number)

            ## Accept/Reject 결정 , Accept 시 stock_item_number에서 재고량 감소.
            Result = input("1. Accept  2.Reject ")
            if Result == 1:
                self.Result.append("Accept")
                for j in range(len(stock_index_list)): # 재고량 감소. DB 반영 x
                    stock_item_number[stock_index_list[j]] -= self.order_list.item_number[j]
            else:
                self.Result.append("Reject")

            ## self.order_list에서 삭제. 파일도 삭제.
            order_file = self.user_id + "_Order\\" + self.order_list[i].order_number + ".txt"
            if os.path.isfile(order_file):
                os.remove(order_file)
            else:
                print("{} is not exist".format(order_file))
        ##  모든 order_list 처리 시 반복 종료

    # 받은 발주 목록 보여주기.
    def showOrderList(self):
        print("Receive order : {}".format(len(self.order_list)))
        for i in range(len(self.order_list)):
            print("{0}. {1}".format((i+1),self.order_list[i].order_number))

    # 선택한 발주 품목, 재고상황 보여주기
    def showOrder(self, index, stock_list_index, stock_number):
        print("{0: <25}|{1: <25}|{2: <25}|{3: <25}".format("item name", "item brand", "order item number", "stock remain #"))
        for i in range(len(self.order_list[index].item_name)): # 해당 인덱스의 발주 품목들 출력
            print("{0: <25}|{1: <25}|{2: <25}|{3: <25}".format(self.order_list[index].item_name[i],self.order_list[index].item_brand[i], 
            self.order_list[index].item_number[i], stock_number[stock_list_index[i]]))
        




            





