from cgitb import html
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HotGoods

# Create your views here.
def home(request):
    hotgoods = HotGoods.objects.all()
    return render(request, 'home.html',{'hotgoods': hotgoods})



 
