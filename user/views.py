from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
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
    return render(request, "user/login.html", {})