import os
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
                print(lines[j][:-1])
            order_file.close() # 다 쓰고 닫아준다.


class ResultTaker:
    def __init__(self,user_id):
        self.user_id = user_id


    def takeResult(self):
        if
        order_num_list = os.listdir()
        
            