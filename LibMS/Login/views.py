from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as djlogin

# Create your views here.
def login (request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            djlogin(request, user)
            return home(request)
        else:
            messages.error(request, 'Not a valid Username of Password !')
    else:
        form = AuthenticationForm()

    return render(request, 'Login/login.html', {'form': form})


def home (request):
    return render(request, 'Home/home.html')