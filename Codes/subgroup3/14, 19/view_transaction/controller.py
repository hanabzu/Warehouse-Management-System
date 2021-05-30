from view_transaction.database_connection import databaseconnection as dbc
from page_maker import pagemaker

class Controller :
    def __init__(self, transaction_info) :
        td = dbc.get_data(transaction_info)
        pagemaker.make_page(td)
