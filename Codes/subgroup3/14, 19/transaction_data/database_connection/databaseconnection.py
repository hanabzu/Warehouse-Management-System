from transaction_data.database_connection.archiever import archiever

class DatabaseConnection :
    def __init__(self, transaction_data) :
        self.__database = open('database.txt', 'a')
        self.input(transaction_data)
        
    def input(self, transaction_data) :
        archiever.Archiever(self.__database, transaction_data)

    def __del__(self) :
        self.__database.close()
