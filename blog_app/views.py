from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


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


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: return True
        return False


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Create'
        return context


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Function working with Userpasses to prevent just anyone from updating post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: return True
        return False


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
