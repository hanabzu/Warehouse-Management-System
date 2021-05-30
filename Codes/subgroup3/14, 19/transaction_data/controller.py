from transaction_data.database_connection import databaseconnection as dbc

class Controller :
    def __init__(self, brand, product, user) :
        self.__transaction_data = {"brand" : brand, "product" : product, "user" : user}
        self.__db = dbc.DatabaseConnection(self.__transaction_data)
        del self.__db
