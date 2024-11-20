from django.shortcuts import render

# Create your views here.
# task3/views.py

from django.shortcuts import render

def games_view(request):
    context = {
        'first': 'Atomic Heart',
        'second': 'Cyberpunk 2077'
    }
    return render(request, 'fourth_task/games.html', context)
def index(request):
    return render(request, 'fourth_task/index.html')
def shop(request):
    return render(request, 'fourth_task/shop.html')
def cart(request):
    return render(request, 'fourth_task/cart.html')
def object_detection(request):
    # Здесь можно добавить логику для обработки данных объектного обнаружения
    return render(request, 'fourth_task/object_detection.html')