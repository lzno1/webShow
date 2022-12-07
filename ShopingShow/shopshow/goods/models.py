from django.db import models

# Create your models here.
class ALLHotGoods(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='img/', blank=True)

class selectDingdans(models.Model):
    time = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    dingdanname = models.CharField(max_length=20, blank=True, null=True)
    upmoney = models.CharField(max_length=20, blank=True, null=True)
    pi = models.CharField(max_length=20, blank=True, null=True)
    com = models.CharField(max_length=100, blank=True, null=True)
    dingdanID = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    money = models.CharField(max_length=20, blank=True, null=True)
    othermoney = models.CharField(max_length=20, blank=True, null=True)
    allmoney = models.CharField(max_length=20, blank=True, null=True)

class Dingdans(models.Model):
    index = models.CharField(max_length=20, blank=True, null=True)
    pi = models.CharField(max_length=20, blank=True, null=True)
    kehu = models.CharField(max_length=20, blank=True, null=True)
    goods = models.CharField(max_length=20, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    money = models.CharField(max_length=20, blank=True, null=True)
    poID = models.CharField(max_length=20, blank=True, null=True)
    poTime = models.CharField(max_length=20, blank=True, null=True)
    label = models.CharField(max_length=20, blank=True, null=True)
    
class CaiGou(models.Model):
    time = models.CharField(max_length=20, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    goods = models.CharField(max_length=20, blank=True, null=True)
    upMoney = models.CharField(max_length=20, blank=True, null=True)
    PI = models.CharField(max_length=20, blank=True, null=True)
    com = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    money = models.CharField(max_length=20, blank=True, null=True)
    otherMoney = models.CharField(max_length=20, blank=True, null=True)
    allMoney = models.CharField(max_length=20, blank=True, null=True)
   