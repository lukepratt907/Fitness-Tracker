from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('users-profile')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('/')

def diary_view(request):
    return render(request, 'users/diary.html', {'user': request.user})

def goal_view(request):
    return render(request, 'users/goals.html', {'user': request.user})