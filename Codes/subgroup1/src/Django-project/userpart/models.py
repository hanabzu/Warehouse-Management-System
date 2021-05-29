from django.db import models

class User_info(models.Model) :
    id = models.CharField(max_length = 20, primary_key = True)
    pw = models.CharField(max_length =20)

class data_AccountInfo(models.Model):
    accountid = models.CharField(max_length = 20, primary_key=True)
    password = models.CharField(max_length = 20)
    position = models.TextField()
    name = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.accountid

class data_TempAccountInfo(models.Model):
    accountid = models.CharField(max_length = 20, primary_key=True)
    password = models.CharField(max_length = 20)
    position = models.TextField()
    name = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.accountid

class data_log(models.Model):
    account = models.ForeignKey(data_AccountInfo, on_delete=models.CASCADE)
    time = models.DateTimeField()
    cond = models.TextField()

    def __str__(self):
        return (self.account, self.time)

#회원가입시 쓰는 임시 클래스
class WebUser(models.Model):
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=10)

