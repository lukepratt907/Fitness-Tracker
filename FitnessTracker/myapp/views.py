from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request, "index.html")

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]
        new_user = authenticate(username=username, email=email, password=password)
        login(request, new_user)
        return redirect("index")

    form = SignUpForm()
    context = {"form":form}
    return render(request, "signup.html", context)

