# user module
from .models import *

def encrypt(accountInfo):
    eA = accountInfo
    
    # encryption of Id, password

    return eA

def decrypt(eA):
    A = eA

    # decryption of Id, password

    return A

def userData(accountInfo):
    A = accountInfo
    if A.flag == True:
        oldA = AccountInfo.obgects.get(pk=A._id)
        oldA.delete()
    newA = AccountInfo(accountid=A._id) # 11:05 check
    
    #dbconnection.saveNew(A)


def authenticateUser(accountInfo):
    A = encrypt(accountInfo)
    



    return ret