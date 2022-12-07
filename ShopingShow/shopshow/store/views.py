from django.shortcuts import render
from .models import Stores
# Create your views here.
def store(request):
    stores = Stores.objects.all()
    return render(request, 'store.html', {'stores': stores})