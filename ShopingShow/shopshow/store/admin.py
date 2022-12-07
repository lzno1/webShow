from django.contrib import admin
from .models import Stores
from .models import customLevel
from .models import customBlacklist
from .models import customInfo
# Register your models here.


class StoresInfo(admin.ModelAdmin):
    list_display = ['name', 'info', 'url', 'img']

class customBlacklistInfo(admin.ModelAdmin):
    list_display = ['index', 'custom', 'email', 'list', 'reason', 'time', 'user', 'remark']

class customLevelInfo(admin.ModelAdmin):
    list_display = ['email', 'level']

class customInfoInfo(admin.ModelAdmin):
    list_display = ['custom', 'email', 'allMoney']

admin.site.register(Stores, StoresInfo)
admin.site.register(customBlacklist, customBlacklistInfo)
admin.site.register(customLevel, customLevelInfo)
admin.site.register(customInfo, customInfoInfo)