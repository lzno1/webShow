from django.db import models

# Create your models here.
class Stores(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    info = models.TextField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='img/', blank=True)


class customBlacklist(models.Model):
    index = models.CharField(max_length=100, blank=True, null=True)
    custom = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    list = models.CharField(max_length=40, blank=True, null=True)
    reason = models.CharField(max_length=40, blank=True, null=True)
    time = models.CharField(max_length=40, blank=True, null=True)
    user = models.CharField(max_length=40, blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)

class customLevel(models.Model):
    email = models.CharField(max_length=40, blank=True, null=True)
    level = models.CharField(max_length=40, blank=True, null=True)
    

class customInfo(models.Model):
    custom = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    allMoney = models.CharField(max_length=40, blank=True, null=True)

