import OrderList

class OrderEditor:
    def __init__(self, order_list):
        self.order_list = order_list # 자동 모드 off일때는 None으로 들어와서 직접 만들 수 있도록.

        if self.order_list == None:
            self.MakeOrder()
        else:
            self.EditOrder()
    def EditOrder(self): # 자동모드 on일때
        pass

    
    


