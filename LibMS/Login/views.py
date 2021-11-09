from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as djlogin

# Create your views here.
@csrf_protect
def login (request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return home(request)
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

#@login_required
@csrf_exempt
def home (request):
    if request.user.is_authenticated:
        return render(request, 'Home/home.html', {'user':request.user})
    else:
        return login(request)
    