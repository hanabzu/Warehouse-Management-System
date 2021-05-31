# user module
from .models import *
from .userclasses import *

class UserModule:
    def encrypt(self,accountInfo):
        key = 60
        eA = accountInfo
        s_password = ''
        for i in range(len(eA._password)):
            c = eA._password[i]
            s_password += chr((ord(c) + key -33) % 94 + 33)
        eA._password = s_password
        return eA

    def decrypt(self,eA):
        key = 60
        A = eA
        s_password = ''
        for i in range(len(A._password)):
            c = A._password[i]
            s_password += chr((ord(c) - key -33) % 94 + 33)
        A._password = s_password
        return A

    def userData(self, accountInfo):
        A = accountInfo
        if A._flag == True:
            oldA = data_AccountInfo.objects.get(pk=A._accountid)
            oldA.delete()
        newA = data_AccountInfo(accountid = A._accountid, password = A._password, position = A._position,\
                            name = A._name, address = A._address)
        newA.save()
        
    def authenticateUser(self, accountInfo):
        A = self.encrypt(accountInfo)
        ca = CompareAccount.CompareAccount()
        ca.compareID(A)
        return ca.returnRet()

    def register(self, accountInfo):
        checkRedundancy = self.authenticateUser(accountInfo)
        if checkRedundancy == "Duplicate":
            return False
        else:
            return True

        
        