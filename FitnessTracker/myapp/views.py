from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request, "index.html")

#def register(request):
#    form = UserCreationForm()
#    return render(request, 'users/register.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get["username"]
            email = form.cleaned_data.get["email"]
            password = form.cleaned_data["password1"]
            new_user = authenticate(username=username, email=email, password=password)
            if new_user is not None:
                login(request, new_user)
            return redirect("index")
    else:
        form = SignUpForm()
    context = {"form":form}
    return render(request, "myapp/signup.html", context)

