import sqlite3

class DatabaseModule:
    def __init__(self):
        self.__Database = sqlite3.connect("database.db")
        self.__cur = self.__Database.cursor()

    def initiate(self):
        self.__cur.execute("CREATE TABLE IF NOT EXISTS \
                            accounts_data(id TEXT PRIMARY KEY, \
                            pw TEXT, position TEXT, name TEXT, address TEXT)")
        self.__cur.execute("CREATE TABLE IF NOT EXISTS \
                            temp_accounts_data(id TEXT PRIMARY KEY, \
                            pw TEXT, position TEXT, name TEXT, address TEXT)")
        self.__cur.execute("CREATE TABLE IF NOT EXISTS \
                            logs_data(time TEXT, id TEXT, cond TEXT, \
                            PRIMARY KEY(time, id))")

    def insertAccount(self, accountInfo):
        self.__cur.execute("INSERT INTO accounts_data(id, pw, position, name, address) \
                            VALUES(?,?,?,?,?)", accountInfo)
    
    def insertTempAccount(self, tempAccountInfo):
        self.__cur.execute("INSERT INTO temp_accounts_data(id, pw, position, name, address) \
                            VALUES(?,?,?,?,?)", tempAccountInfo)

    def insertLog(self, log):
        self.__cur.execute("INSERT INTO logs_data(time, id, cond) \
                            VALUES(?,?,?)", log)
