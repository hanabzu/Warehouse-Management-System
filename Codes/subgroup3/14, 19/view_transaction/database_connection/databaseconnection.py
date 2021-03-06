def get_data(transaction_info) :
    try :
        database = open('database.txt', 'r')
        
    except :
        database = open('database.txt', 'w')
        database.close()
        
        return []
    
    else :
        datas = database.readlines()

        result = []
        start = transaction_info.get('period')[0]
        end   = transaction_info.get('period')[1]
                        
        for data in datas :
            data = data.split(' ')

            if start <= data[4] and data[4] <= end :
                if transaction_info.get('user')[0] == 'admin' :
                    if transaction_info.get('relation') == 1 :
                        if data[0] == 'warehouse' :
                            result.append(data)
                        
                    elif transaction_info.get('relation') == 2 :
                        if data[0] == 'shop' :
                            result.append(data)
        
                elif transaction_info.get('user')[0] == 'warehouse' :
                    if transaction_info.get('relation') == 1 :
                        if data[0] == 'warehouse' and data[1] == transaction_info.get('user')[1] : 
                            result.append(data)
                            
                    elif transaction_info.get('relation') == 2 :
                        if data[2] == 'warehouse' and data[3] == transaction_info.get('user')[1] :
                            result.append(data)
                            
                elif transaction_info.get('user')[0] == 'shop' :
                    if data[0] == 'shop' and data[1] == transaction_info.get('user')[1] :
                        result.append(data)

        
        database.close()

        return result
