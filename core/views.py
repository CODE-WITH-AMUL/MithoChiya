from django.shortcuts import render
from .models import MenuItem
# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    items = MenuItem.objects.all()
    context = {
        'items':items
    }
    return render(request,'menu/menu.html' , context)