from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  # Показывать 5 постов на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})
# blog/views.py
def post_list(request):
    post_list = Post.objects.all()
    items_per_page = request.GET.get('items_per_page', 5)  # По умолчанию 5
    paginator = Paginator(post_list, items_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})