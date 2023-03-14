from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            users = form.save()
            login(request, users)
            messages.success(request, "Registration successful.")
            return redirect("user:login")
        
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, "user/register.html", context)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, ("There was an an error Logging in, Try again..."))
            return redirect("login")
    else:
        return render(request, "user/login.html", {})