import datetime


class Datecounter:
    def __init__(self, oreder_date, n_day):
        self.order_date = oreder_date
        self.n_day = n_day

    def DateCheck(self): # 오늘이 발주 n 일 전인지
        today = datetime.date.today()
        today = today.day
        if self.order_date - self.n_day <= today and self.order_date > today: # n일전 ~ 발주날짜 전날 까지
            return True
        else:
            return False

    def OrderDateCheck(self): # 오늘이 발주 날짜인지
        today = datetime.date.today()
        today = today.day
        if self.order_date == today:
            return True
        else:
            return False
