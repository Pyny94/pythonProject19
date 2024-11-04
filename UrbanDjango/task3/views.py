from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    return render(request, 'third_task/platform.html')

def shop(request):
    shop_items = {
        'item1': 'Игра 1',
        'item2': 'Игра 2',
        'item3': 'Игра 3',
    }
    return render(request, 'third_task/games.html', {'shop_items': shop_items})

def cart(request):
    return render(request, 'third_task/cart.html')