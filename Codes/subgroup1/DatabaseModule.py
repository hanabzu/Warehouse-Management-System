import sqlite3

class DatabaseModule:
    def __init__(self):
        self.__Database = sqlite3.connect("database.db")
        self.__curDatabase = self.__Database.cursor()

    def initiate(self):
        self.__Database.excute("CREATE TABLE accounts_data(id TEXT PRIMARY KEY, \
                                pw TEXT, position TEXT, name TEXT, address TEXT)")
        self.__Database.excute("CREATE TABLE temp_accounts_data(id TEXT PRIMARY KEY, \
                                pw TEXT, position TEXT, name TEXT, address TEXT)")
        self.__Database.excute("CREATE TABLE logs_data(time TEXT, id TEXT, cond TEXT, \
                                PRIMARY KEY(time, id))")
