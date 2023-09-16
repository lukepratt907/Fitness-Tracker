from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, UserCreationForm
# Create your views here.

def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")