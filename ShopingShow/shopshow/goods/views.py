from django.shortcuts import render
from .models import ALLHotGoods
from .models import Dingdans

# Create your views here.
def goods(request):
    allhotgoods = ALLHotGoods.objects.all()
    return render(request, 'goods.html', {'hotgoods': allhotgoods})

def dingdans(request):
    dingdan = Dingdans.objects.all()
    return render(request, 'goods.html', {'dingdan': dingdan})