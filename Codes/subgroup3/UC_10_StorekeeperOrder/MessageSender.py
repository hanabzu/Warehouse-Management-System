## admin이 주문을 보고 승인/거절 결정. stub으로 이용.

import os
class MessageSender:
    def __init__(self, order_num):
        self.order_num = order_num

    def AcceptOrder(self):
        if os.path.isdir(os.getcwd() + '\\' + self.user_id + "_Order") == False:
            os.mkdir(os.getcwd() + '\\' + self.user_id + "_Order")
        file = open(os.getcwd() + '\\' + self.user_id + "_Order\\" +self.order_num + '.txt', 'r', encoding='utf8')
        lines = file.readlines()
        lines[0] = 'Accept' # 승인으로 변경
        file.close()
        file = open(os.getcwd() + '\\' + self.user_id + "_Order\\" +self.order_num + '.txt', 'w', encoding='utf8')
        for line in lines:
            print(line.rstrip('\n'), file= file)
        file.close()
    def RejectOrder(self):
        if os.path.isdir(os.getcwd() + '\\' + self.user_id + "_Order") == False:
            os.mkdir(os.getcwd() + '\\' + self.user_id + "_Order")
        file = open(os.getcwd() + '\\' + self.user_id + "_Order\\" +self.order_num + '.txt', 'r', encoding='utf8')
        lines = file.readlines()
        lines[0] = 'Reject' # 승인으로 변경
        file.close()
        file = open(os.getcwd() + '\\' + self.user_id + "_Order\\" +self.order_num + '.txt', 'w', encoding='utf8')
        for line in lines:
            print(line.rstrip('\n'), file= file)
        file.close()

    def TakeResult(self):
        if os.path.isdir(os.getcwd() + '\\' + self.user_id + "_Order") == False:
            print("주문 신청한 목록이 없습니다.")
        order_file = os.listdir(os.getcwd() + '\\' + self.user_id + "_Order") # 주문은 한번 발송. 2개 이상 쌓여있지 않다.
        file = open(os.getcwd() + '\\' + self.user_id + "_Order\\" + order_file[0], 'r', encoding='utf8')
        lines = file.readlines()
        if lines[0].rstrip('\n') == 'Accept':
            print("발주가 성공적으로 신청되었습니다.")
            result = 'Accept'
        elif lines[0].rstrip('\n') == 'Reject':
            print("발주가 거절되었습니다.")
            result = 'Reject'
        elif lines[0].rstrip('\n') == 'Ready':
            print("발주가 아직 접수 되지 않았습니다.")
            result = 'Ready'
        else:
            print("error, 발주 과정에서 문제 발생.")
            result = 'Error'
        file.close()
        return result, order_file[0][:-4] #결과와 주문번호를 반환.