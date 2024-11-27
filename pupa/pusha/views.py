from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib import messages
from .forms import ImageUploadForm
from .models import ImageUpload
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from .forms import UploadImageForm  # Предполагается, что у вас есть форма для загрузки изображений
from .utils import recognize_image

def recognize_image(file_path):
    # Загружаем предварительно обученную модель MobileNetV2
    model = MobileNetV2(weights='imagenet')

    # Загружаем изображение и изменяем его размер до 224x224 пикселей
    img = image.load_img(file_path, target_size=(224, 224))

    # Преобразуем изображение в массив numpy
    img_array = image.img_to_array(img)

    # Добавляем измерение (batch dimension)
    img_array = np.expand_dims(img_array, axis=0)

    # Предобрабатываем изображение
    img_array = preprocess_input(img_array)

    # Предсказание
    predictions = model.predict(img_array)

    # Декодируем предсказания
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    return decoded_predictions

import io
def home_view(request):
    return render(request, 'pusha/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Перенаправление на панель управления после успешного входа
        else:
            return HttpResponse("Invalid login credentials")
    return render(request, 'pusha/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please choose a different one.")
                return redirect('register')

            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "User registered successfully.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "An error occurred during registration. Please try again.")
            return redirect('register')

    return render(request, 'pusha/register.html')

@login_required(login_url='/object_detection/login')
def object_detection_view(request):
    return render(request, 'pusha/object_detection.html')
@login_required
def dashboard_view(request):
    context = {}
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']
            # Сохраняем загруженное изображение
            file_path = f'media/{image_file.name}'
            with open(file_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            # Распознаем объекты на изображении
            predictions = recognize_image(file_path)

            # Передаем предсказания в контекст
            context['predictions'] = predictions

    else:
        form = UploadImageForm()

    context['form'] = form
    return render(request, 'pusha/dashboard.html', context)

@login_required(login_url='login')
def add_image_feed_view(request):
    # Здесь будет логика для добавления изображения в ленту
    return render(request, 'pusha/add_image_feed.html')

def redirect_to_register(request):
    return redirect('register')