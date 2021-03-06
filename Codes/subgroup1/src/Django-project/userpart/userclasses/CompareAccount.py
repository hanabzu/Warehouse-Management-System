from datetime import datetime
from ..models import *

class CompareAccount:
    def __init__(self):
        self.__dAs = data_AccountInfo.objects.all()
        self.__ret = "NoMatch"

    def compareID(self, A):
        for dA in self.__dAs:
            if dA.accountid == A._accountid:
                if A._register == True:
                    self.__ret = "Duplicate"
                else:
                    self.comparePW(dA,A)

    def comparePW(self, dA, A):
        if dA.password == A._password:
            A._position = dA.position
            self.__ret = "Agree"
        else:
            self.__ret = "Refuse"
        self.saveLog(dA)
        
    def saveLog(self, accountInfo):
        # saveLog to models
        log = data_log(account = accountInfo, time = datetime.now(), cond = self.__ret)
        log.save()

    def returnRet(self):
        return self.__ret







