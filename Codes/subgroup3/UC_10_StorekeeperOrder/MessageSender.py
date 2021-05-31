## admin이 주문을 보고 승인/거절 결정. stub으로 이용.


class MessageSender:
    def __init__(self, order_num):
        self.order_num = order_num

    def AcceptOrder(self):
        file = open(self.order_num + '.txt', 'r', encoding='utf8')
        lines = file.readlines()
        lines[0] = 'Accept' # 승인으로 변경
        file.close()
        file = open(self.order_num + '.txt', 'w', encoding='utf8')
        for line in lines:
            print(line.rstrip('\n'), file= file)
        file.close()
    def RejectOrder(self):
        file = open(self.order_num + '.txt', 'r', encoding='utf8')
        lines = file.readlines()
        lines[0] = 'Reject' # 승인으로 변경
        file.close()
        file = open(self.order_num + '.txt', 'w', encoding='utf8')
        for line in lines:
            print(line.rstrip('\n'), file= file)
        file.close()
