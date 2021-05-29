import OrderListMaker as olm


class sh_user:
    def __init__(self, type,id, connected,money):
        self.id = id
        self.type = type
        self.connected = connected
        self.money = money

class wh_user:
    def __init__(self, type,id, connected,money,auto_mode = 'on'):
        self.id = id
        self.type = type
        self.connected = connected
        self.money = money
        self.mode = auto_mode


class controller:
    def __init__(self, user):
        self.user = user
        self.price = 0
        self.result = None
        self.MakeOrder()
    
    def MakeOrder(self):
        OrderListMaker = olm.OrderListMaker("w20210527")
        self.price = OrderListMaker.getPrice()



#driver
class initiator:
    def __init__(self):
        user_type = input("1. 창고주 / 2. 점주 ")
        user_info = []
        if user_type == 1:
            user_info.append("warehouse")
            info_file = open("창고주.txt", "r", encoding="utf8")
            for i in range(4):
                line = info_file.readline()
                temp = line.split(' ')
                user_info.append(temp[2][:-1])
            now_user = wh_user(user_info[0],user_info[1],user_info[2],user_info[3], user_info[4])
        else:
            user_info.append("shop")
            info_file = open("점주.txt", "r", encoding="utf8")
            for i in range(3):
                line = info_file.readline()
                temp = line.split(' ')
                user_info.append(temp[2][:-1])
            now_user = sh_user(user_info[0],user_info[1],user_info[2],user_info[3])
        
        controller(now_user)


# initiator()
# user_info = []
# info_file = open("창고주.txt", "r", encoding="utf8")
# user_info.append("warehouse")
# for i in range(4):
#     line = info_file.readline()
#     temp = line.split(' ')
#     user_info.append(temp[2][:-1])
# now_user = wh_user(user_info[0],user_info[1],user_info[2],user_info[3], user_info[4])

# print(now_user.connected, now_user.id, now_user.mode, now_user.money, now_user.type)