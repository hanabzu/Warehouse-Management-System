from transaction_data import controller

def transaction_data(brand, product, user) :
    transaction_data = {"brand" : brand, "product" : product, "user" : user}
    controller.Controller(transaction_data)
