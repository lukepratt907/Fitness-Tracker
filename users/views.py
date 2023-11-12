from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import LoginForm, UserRegisterForm, DiaryForm, ReminderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DiaryEntry, Reminder
from django.views.decorators.cache import cache_control


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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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


def reminder_view(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect('users-reminder')
        else:
            return redirect('users-reminder')
    else:
        reminders = Reminder.objects.filter(user=request.user)
        form = ReminderForm()
        return render(request, 'users/reminder.html', {'user': request.user, 'reminders': reminders, 'form': form})