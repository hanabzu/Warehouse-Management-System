# user module
from .models import *
from .userclasses import *

class UserModule:
    def encrypt(self,accountInfo):
        eA = accountInfo
        
        # encryption of Id, password

        return eA

    def decrypt(self,eA):
        A = eA

        # decryption of Id, password

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

        
        