from django.contrib import admin
from .models import HotGoods
# Register your models here.


class HotGoodsInfo(admin.ModelAdmin):
    list_display = ['name', 'price', 'url', 'img']
admin.site.site_title = '用户名'
admin.site.register(HotGoods, HotGoodsInfo)