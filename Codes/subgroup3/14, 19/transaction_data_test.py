from transaction_data import transactiondata
import time

user = ('warehouse', '10000001', '00000000')
transactiondata.transaction_data(brand = "seoul", product = "milk", user = user)
transactiondata.transaction_data(brand = "ghana", product = "chocolate", user = user)

user = ('shop', '10000002', '10000001')
transactiondata.transaction_data(brand = "beer", product = "kloud", user = user)
transactiondata.transaction_data(brand = "delmonte", product = "orange juice", user = user)
