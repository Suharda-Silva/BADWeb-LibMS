from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login as djlogin

# Create your views here.
@csrf_protect
def login (request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('../')
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            djlogin(request, user)
            return redirect('../')
        else:
            messages.error(request, 'Not a valid Username or Password !')
    else:
        form = AuthenticationForm()

    return render(request, 'Login/login.html', {'form': form})


    