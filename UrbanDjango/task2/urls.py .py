from django.urls import path
from .views import function_based_view, ClassBasedView

urlpatterns = [
    path('function/', function_based_view, name='function_based'),
    path('class/', ClassBasedView.as_view(), name='class_based'),
]