from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .forms import LoginForm, UserRegisterForm, DiaryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import DiaryEntry
import logging

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

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
    logger = logging.getLogger(__name__)
    logger.debug(request.POST)
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary_entry = form.save(commit=False)
            diary_entry.user = request.user
            diary_entry.save()
            return redirect('users-diary')
        else:
            logger.error(f"Form Errors: {form.errors}")
            return render(request, 'users/diary_entry.html', {'form': form})
    else:
        logger.error("Invalid request type")
        form = DiaryForm()
        return render(request, 'users/diary_entry.html', {'form': form})

def goal_view(request):
    return render(request, 'users/goals.html', {'user': request.user})