from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import LoginForm, UserRegisterForm, DiaryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DiaryEntry


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

def diary_list(request):
    diaries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'users/diary.html', {'diaries': diaries})

def diary_detail(request, pk):
    diary = get_object_or_404(DiaryEntry, pk=pk)
    return render(request, 'users/diary_detail.html', {'diary': diary})

def create_diary_entry(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            date = request.date
            title = request.title
            content = request.content

            return redirect('users-diary', {'user': user, 'date': date, 'title': title, 'content': content})
    else:
        form = DiaryForm()
    return render(request, 'users/diary_entry.html', {'form': form})

def goal_view(request):
    return render(request, 'users/goals.html', {'user': request.user})