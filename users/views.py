from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Get the details from the form
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            confirmation = form.cleaned_data.get('password2')

            # Ensure password matches confirmation
            if password != confirmation:
                return render(request, "users/register.html", {
                    "message": "Passwords must match."
                })

            # Attempt to create a new user
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                return render(request, "users/register.html", {
                    "message": "Username already taken."
                })

            login(request, user)
            return redirect('users-profile')
        else:
            return render(request, "users/register.html", {'form': form})
    else:
        form = SignUpForm()
        return render(request, "users/register.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile.html')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('/')


