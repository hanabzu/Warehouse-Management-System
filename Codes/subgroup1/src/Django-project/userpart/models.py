from django.db import models

<<<<<<< HEAD
# Create your models here.

class User_info(models.Model) :
    id = models.CharField(max_length = 20, primary_key = True)
    pw = models.CharField(max_length =20)
=======
class AccountInfo(models.Model):
    accountid = models.CharField(max_length = 20, primary_key=True)
    password = models.CharField(max_length = 20)
    position = models.TextField()
    name = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.accountid

class tempAccountInfo(models.Model):
    accountid = models.CharField(max_length = 20, primary_key=True)
    password = models.CharField(max_length = 20)
    position = models.TextField()
    name = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.accountid

class log(models.Model):
    account = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)
    time = models.DateTimeField()
    cond = models.TextField()

    def __str__(self):
        return (self.account, time)
>>>>>>> 804000aedb82f52221d314bd22324b563fbe524e
