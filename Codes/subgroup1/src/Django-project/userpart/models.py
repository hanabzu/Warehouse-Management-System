from django.db import models

class AccountInfo(models.Model):
    accountid = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    position = models.TextField()
    name = models.TextField()
    address = models.TextField()

class tempAccountInfo(models.Model):
    accountid = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    position = models.TextField()
    name = models.TextField()
    address = models.TextField()

class log(models.Model):
    account = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)
    time = models.DateTimeField()
    cond = models.TextField()