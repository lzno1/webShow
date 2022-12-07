from django.contrib import admin
from .models import ALLHotGoods
from .models import Dingdans
from .models import selectDingdans
from .models import CaiGou
# Register your models here.
class HotGoodsInfo(admin.ModelAdmin):
    list_display = ['name', 'price', 'url', 'img']

class DingdansINFO(admin.ModelAdmin):
    list_display = ['index', 'pi', 'kehu', 'goods', 'user', 'money', 'poID', 'poTime', 'label']


class SelectDingdansINFO(admin.ModelAdmin):
    list_display = ['time', 'username', 'dingdanname', 'upmoney', 'pi', 'com', 'dingdanID', 'type', 'num', 'money', 'othermoney', 'allmoney']

class CaiGouInfo(admin.ModelAdmin):
    list_display = ['time', 'user', 'goods', 'upMoney', 'PI', 'com', 'phone', 'type', 'num', 'money', 'otherMoney', 'allMoney']



admin.site.register(ALLHotGoods, HotGoodsInfo)
admin.site.register(Dingdans, DingdansINFO)
admin.site.register(selectDingdans, SelectDingdansINFO)
admin.site.register(CaiGou, CaiGouInfo)