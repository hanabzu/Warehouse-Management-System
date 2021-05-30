class Archiever :
    def __init__(self, database, transaction_data) :
        self.add(database, transaction_data)
        
    def add(self, database, transaction_data) :
        if transaction_data.get("user")[0] == "warehouse" :
            database.write(transaction_data.get("user")[0] + " " + \
                           str(transaction_data.get("user")[1]) + " " + \
                           "admin" + " " + \
                           str(transaction_data.get("user")[2]) + " " + \
                           transaction_data.get("brand") + " " + \
                           transaction_data.get("product") + "\n")

        elif transaction_data.get("user")[0] == "shop" :
            database.write(transaction_data.get("user")[0] + " " + \
                           str(transaction_data.get("user")[1]) + " " + \
                           "warehouse" + " " + \
                           str(transaction_data.get("user")[2]) + " " + \
                           transaction_data.get("brand") + " " + \
                           transaction_data.get("product") + "\n")
