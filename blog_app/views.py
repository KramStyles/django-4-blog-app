from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# def index(request):
#     posts = Post.objects.all()
#     context = {
#         'title': 'home',
#         'blogs': posts
#     }
#     return render(request, 'blog/index.html', context)


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'blog_posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'home'
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'blog'


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
