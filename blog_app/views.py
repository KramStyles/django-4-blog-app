from turtle import pos
from django.shortcuts import render, HttpResponse

from .models import Post

def index(request):
    post = Post.objects.all()
    context = {
        'title': 'home',
        'blogs': post
    }
    return render(request, 'blog/index.html', context)


def about(request):
    context = {
        'title': 'about'
    }
    return render(request, 'blog/about.html', context)


def post(request):
    context = {
        'title': 'blog'
    }
    return render(request, 'blog/post.html', context)
