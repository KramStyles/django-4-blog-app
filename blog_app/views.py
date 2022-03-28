from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'blog/index.html')


def about(request):
    return HttpResponse('<h2>Project_4_Blog About page </h2>')
