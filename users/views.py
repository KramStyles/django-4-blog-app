from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"User: {username} registered")
            return redirect('blog_home')
        else:
            messages.warning(request, 'Wrong Form Info')
    else: form = UserCreationForm()
    context = {
        'form': form,
        'title': 'Register Users'
    }
    return render(request, 'users/register.html', context)
