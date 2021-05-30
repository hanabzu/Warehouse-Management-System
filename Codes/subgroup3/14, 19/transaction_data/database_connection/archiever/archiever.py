import time

def add(database, transaction_data) :
    t = time.localtime(time.time())
    
    if transaction_data.get("user")[0] == "warehouse" :
        database.write(transaction_data.get("user")[0] + " " + \
                       str(transaction_data.get("user")[1]) + " " + \
                       "admin" + " " + \
                       str(transaction_data.get("user")[2]) + " " + \
                       str(t.get('tm_year')) + \
                       str(t.get('tm_mon')) + \
                       str(t.get('tm_day')) + ' ' + \
                       transaction_data.get("brand") + " " + \
                       transaction_data.get("product") + "\n")

    elif transaction_data.get("user")[0] == "shop" :
        database.write(transaction_data.get("user")[0] + " " + \
                       str(transaction_data.get("user")[1]) + " " + \
                       "warehouse" + " " + \
                       str(transaction_data.get("user")[2]) + " " + \
                       str(t.get('tm_year')) + \
                       str(t.get('tm_mon')) + \
                       str(t.get('tm_day')) + ' ' + \
                       transaction_data.get("brand") + " " + \
                       transaction_data.get("product") + "\n")
