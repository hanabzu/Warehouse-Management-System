from transaction_data.database_connection import databaseconnection as dbc

class Controller :
    def __init__(self, transaction_data) :
        dbc.DatabaseConnection(self.__transaction_data)
        
