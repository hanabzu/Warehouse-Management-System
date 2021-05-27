import UC_09_ShopkeeperOrder


class controller:
    def __init__(self, user):
        self.user = user
        self.price = 0
        self.result = None
    
    def MakeOrder(self):
        OrderListMaker = OrderListMaker()

