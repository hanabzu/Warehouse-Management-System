

class MoneyChecker:
    def __init__(self, total_price):
        self.total_price = total_price

    def checkBalance(self):
        # 파일 읽어서 잔고 가져오기.
        file = open("창고주.txt", 'r',  encoding='utf8')
        lines = file.readlines()
        file.close()
        for line in lines:
            temp = line.rstrip('\n').split(' ')
            if temp[0] == 'money':
                user_money = temp[-1]
            else:
                pass

        if user_money >= self.total_price:
            return True
        else:
            return False
