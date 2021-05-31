class AccountInfo:
    def __init__(self, accountInfo = None):
        if accountInfo:
            self._accountid = accountInfo[0]
            self._password = accountInfo[1]
            self._flag = accountInfo[2]
            self._position = accountInfo[3]
            self._name = accountInfo[4]
            self._address = accountInfo[5]
            self._register = accountInfo[6]
        else:
            self._accountid = ''
            self._password = ''
            self._flag = False
            self._position = ''
            self._name = ''
            self._address = ''
            self._register = False

    def getAccountInfo(self):
        return (self._accountid, self._password, self._flag, self._position, self._name, self._address, self._register)
