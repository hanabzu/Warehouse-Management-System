from ..models import *

class CompareAccount:
    def __init__(self):
        self.__dAs = data_AccountInfo.objects.all()
        self.__ret = "NoMatch"

    def compareID(self, A):
        for dA in self.dAs:
            if dA.accountid == A._accountid:
                self.comparePW(self,dA,A)

    def comparePW(self, dA, A):
        if dA.password == A._password:
            self.__ret = "Agree"
        else:
            self.__ret = "Refuse"
        self.saveLog(self, dA)

    def saveLog(self, dA):
        #saveLog to models
        








