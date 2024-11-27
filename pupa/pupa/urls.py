"""
URL configuration for pupa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# pupa/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from pusha import views  # Предполагается, что ваше приложение называется "pusha"
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Административный интерфейс Django
    path('admin/', admin.site.urls),

    # Домашняя страница
    path('', views.home_view, name='home'),

    # Регистрация пользователя
    path('register/', views.register_view, name='register'),

    # Панель управления (доступна только аутентифицированным пользователям)
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Страница логина
    path('login/', views.login_view, name='login'),

    # Страница выхода из системы
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Добавление изображений в ленту
    path('add_image_feed/', views.add_image_feed_view, name='add_image_feed'),

    # Страница логина для object_detection (если отличается от основной страницы логина)
    path('object_detection/login/', views.login_view, name='object_detection_login'),

    # Маршрут для страницы, защищенной аутентификацией
    path('object_detection/', views.object_detection_view, name='object_detection'),

    # Перенаправление на регистрацию (если требуется)
    path('redirect_to_register/', views.redirect_to_register, name='redirect_to_register'),
    path('logout/', LogoutView.as_view(next_page='register'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)