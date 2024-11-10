from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'fourth_task/platform.html')

def shop(request):

    context =  {'games': ['Atomic Heart', "Cyberpunk 2077"]}
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')

def menu(request):
    return render(request, 'fourth_task/menu.html')