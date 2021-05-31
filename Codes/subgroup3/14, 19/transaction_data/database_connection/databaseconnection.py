from transaction_data.database_connection.archiever import archiever
        
def input(transaction_data) :
    database = open('database.txt', 'a')
    archiever.add(database, transaction_data)
    database.close()
