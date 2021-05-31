

class OrderDate:
    def __init__(self, order_date, n_day):
        self.n_day = n_day # n 일전에 발주 목록 생성 알려주기 위해서 입력되는 n.
        self.date = order_date

    def printOD(self):
        print("발주 날짜 : {}".format(self.date))
        print("{} 일 전에 발주 생성 (자동 모드시)".format(self.n_day))