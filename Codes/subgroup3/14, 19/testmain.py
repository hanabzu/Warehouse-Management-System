from transaction_data import transactiondata
from view_transaction import viewtransaction
import time

user = ('warehouse', '10000001', '00000000')
transactiondata.transaction_data("농심", "신라면", user)
user = ('shop', '10000002', '10000001')
transactiondata.transaction_data("농심", "신라면", user)
user = ('admin', '00000000', '00000000')
viewtransaction.view_transaction(user)
