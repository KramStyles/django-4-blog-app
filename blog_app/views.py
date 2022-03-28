from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<h2>Welcome to My blog</h2>')
