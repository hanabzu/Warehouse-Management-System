class AccountInfo:
    def __init__(self, accountInfo = None):
        if accountInfo:
            self._id = accountInfo[0]
            self._pw = accountInfo[1]
            self._flag = accountInfo[2]
            self._position = accountInfo[3]
            self._name = accountInfo[4]
            self._address = accountInfo[5]
        else:
            self._id = ''
            self._pw = ''
            self._flag = False
            self._position = ''
            self._name = ''
            self._address = ''

    def getAccountInfo(self):
        return (self._id, self._pw, self._flag, self._position, self._name, self._address)
