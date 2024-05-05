from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from user.forms import *
# Create your views here.


def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form['username'].value()
            password = form['password'].value()

        usuario = auth.authenticate(
            request,
            username = name,
            password = password
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'You are successfully logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Incorrect username or password')
            return redirect('login')

    return render(request, 'user/login.html', {'form': form})


def signup(request):
    pass


def logout(request):
    pass
