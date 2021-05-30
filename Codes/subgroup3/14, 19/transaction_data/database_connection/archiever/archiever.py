import time

def add(database, transaction_data) :
    t = time.strftime('%Y%m%d', time.localtime(time.time()))
    
    if transaction_data.get("user")[0] == "warehouse" :
        database.write(transaction_data.get("user")[0] + " " + \
                       transaction_data.get("user")[1] + " " + \
                       "admin" + " " + \
                       transaction_data.get("user")[2] + " " + \
                       t + ' ' + \
                       transaction_data.get("brand") + " " + \
                       transaction_data.get("product") + "\n")

    elif transaction_data.get("user")[0] == "shop" :
        database.write(transaction_data.get("user")[0] + " " + \
                       transaction_data.get("user")[1] + " " + \
                       "warehouse" + " " + \
                       transaction_data.get("user")[2] + " " + \
                       t +' ' + \
                       transaction_data.get("brand") + " " + \
                       transaction_data.get("product") + "\n")
