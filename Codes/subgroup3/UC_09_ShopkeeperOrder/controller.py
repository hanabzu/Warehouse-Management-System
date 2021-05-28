import OrderListMaker as olm
class controller:
    def __init__(self, user):
        self.user = user
        self.price = 0
        self.result = None
    
    def MakeOrder(self):
        OrderListMaker = olm.OrderListMaker("w20210527")
        self.price = OrderListMaker.getPrice()



# test = controller("점주")
# test.MakeOrder()
# print(test.price)