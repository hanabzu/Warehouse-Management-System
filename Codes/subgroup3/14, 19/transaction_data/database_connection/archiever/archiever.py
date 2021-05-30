import time

def add(database, transaction_data) :
    t = time.localtime(time.time())
    t = str(t.get('tm_year')) + \
        '0' if t.get('tm_mon') < 10 else '' + \
        str(t.get('tm_mon')) + \
        '0' if t.get('tm_day') < 10 else '' + \
        str(t.get('tm_day'))
    
    if transaction_data.get("user")[0] == "warehouse" :
        database.write(transaction_data.get("user")[0] + " " + \
                       str(transaction_data.get("user")[1]) + " " + \
                       "admin" + " " + \
                       str(transaction_data.get("user")[2]) + " " + \
                       t + \
                       transaction_data.get("brand") + " " + \
                       transaction_data.get("product") + "\n")

    elif transaction_data.get("user")[0] == "shop" :
        database.write(transaction_data.get("user")[0] + " " + \
                       str(transaction_data.get("user")[1]) + " " + \
                       "warehouse" + " " + \
                       str(transaction_data.get("user")[2]) + " " + \
                       t + \
                       transaction_data.get("brand") + " " + \
                       transaction_data.get("product") + "\n")
