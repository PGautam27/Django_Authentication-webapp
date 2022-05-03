from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect("/")
        else:
            return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return render(request, "index.html")
