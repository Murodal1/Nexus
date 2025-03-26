from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print("USER", user)
            if user:
                login(request, user)
                return redirect('main')
    form = LoginForm()
    ctx = {
        "form": form
    }
    return render(request, 'login.html', ctx)

def register(request):
    pass


def logout_view(request):
    logout(request)
    return redirect('main')

