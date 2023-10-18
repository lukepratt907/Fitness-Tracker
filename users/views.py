from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, UserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users/profile.html')
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile.html')
    else:
        form = LoginForm()
    return render(request, 'users/index.html', {'form': form})


def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('/')


