
class MoneyChanger:
    def __init__(self, price, result, user_id):
        self.price_list = price
        self.user_id = user_id
        self.result = result
    
    def changeMoney(self):
        file = open("점주.txt", 'r', encoding='utf8')
        lines = file.readlines()
        file.close()

        file= open("점주.txt", "w", encoding='utf8')
        for i in range(0, len(lines)-1):
            print(lines[i].rstrip('\n'))
        
        temp = lines[-1].split(' ')
        money = int(temp[2])
        for i in range(len(self.result)):
            if self.result[i] == 'Accept':
                money -= self.price_list[i]
            else:
                pass
        print("{} {} {}".format(temp[0], temp[1], money), file = file)

        print("balance update!")