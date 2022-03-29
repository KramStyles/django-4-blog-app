from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    context = {
        'form': UserCreationForm()
    }
    return render(request, 'users/register.html', context)
