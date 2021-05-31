import os
from . import OrderList
class ResultSender:
    def __init__(self, sender_list, Result, order_number):
        self.sender_list = sender_list
        self.order_number = order_number
        self.Result = Result
    
    def sendResult(self):
        for i in range(len(self.sender_list)):
            order_file = open(self.sender_list[i] + "_Order\\" + self.order_number[i] + ".txt", "r", encoding="utf8") # 기존 order파일 열고
            lines = order_file.readlines() # 기존 내용 모두 담아와서
            order_file.close() # 닫고
            order_file = open(self.sender_list[i] + "_Order\\" + self.order_number[i] + ".txt", "w", encoding="utf8") # 쓰기 모드로 열고
            if self.Result[i] == "Accept": # 결과가 Accept - 파일 상단에 결과 위치.(기존에는 Ready)
                print("Accept", file=order_file)                
            else:                          #결과가 Reject
                print("Reject", file=order_file)

            # 기존파일에 있던 발주 목록 재 입력.
            for j in range(1,len(lines)):
                print(lines[j].rstrip('\n'), file = order_file)
            order_file.close() # 다 쓰고 닫아준다.


class ResultTaker:
    def __init__(self,user_id):
        self.user_id = user_id


    def takeResult(self):
        result = []
        order_list = []

        if os.path.isdir(os.getcwd() + '\\' + self.user_id + "_Order") == False:
            print("no order!")
            return order_list, result
        order_num_list = os.listdir(os.getcwd() +'\\'+ self.user_id + "_Order") # user가 신청한 발주 목록(주문번호.txt).
        for order in order_num_list:
            file = open(os.getcwd() +'\\' + self.user_id + '_Order\\' + order, 'r', encoding='utf8')
            result.append(file.readline().rstrip('\n')) # 첫 줄이 결과
            # 나머지 파일 내용은 발주 목록. OrderList로 만들어서 반환 위해 OrderList화.
            lines = file.readlines()
            item_name = []
            item_brand = []
            item_price = []
            item_number = []
            for i in range(len(lines)):
                temp = lines[i].split(' ')
                item_name.append(temp[0])
                item_brand.append(temp[1])
                item_price.append(int(temp[2]))
                item_number.append(int(temp[3]))
            order_list.append(OrderList.OrderList(item_name[:],item_brand[:], item_price[:], item_number[:], order[:-4])) # order에서 .txt를 빼면 주문번호.
            file.close()
        return order_list, result

        
            