from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def object_detection(request):
    return render(request, 'third_task/object_detection.html')

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = ['Товар 1', 'Товар 2', 'Товар 3']
    context = {'items': items}
    return render(request, 'third_task/shop.html', context)

def cart(request):
    return render(request, 'third_task/cart.html')