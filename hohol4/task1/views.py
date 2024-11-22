from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# task3/views.py

from django.shortcuts import render
from forms import UserRegister

def games_view(request):
    context = {
        'first': 'Atomic Heart',
        'second': 'Cyberpunk 2077'
    }
    return render(request, 'task1/games.html', context)
def index(request):
    return render(request, 'task1/index.html')
def shop(request):
    return render(request, 'task1/shop.html')
def cart(request):
    return render(request, 'task1/cart.html')
def home(request):
    return render(request, 'task1/home.html')

def product_list(request):
    return render(request, 'task1/product_list.html')


def object_detection(request):
    # Здесь можно добавить логику для обработки данных объектного обнаружения
    return render(request, 'task1/object_detection.html')
def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, 'task1/registration_page.html', {'message': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'task1/registration_page.html', info)

def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        try:
            age = int(age)
        except ValueError:
            age = 0

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

        return render(request, 'fifth_task/registration_page.html', info)