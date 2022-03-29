from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"User: {username} registered")
            form.save()
            return redirect('login')
    else: form = RegisterForm()
    context = {
        'form': form,
        'title': 'Register Users'
    }
    return render(request, 'users/register.html', context)
