from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from user.forms import *
# Create your views here.


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

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
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            if form['password1'].value() != form['password2'].value():
                messages.error(request, 'Invalid password')
                return redirect('signup')

            username = form['username'].value()
            password = form['password2'].value()
            email = form['email'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                return redirect('signup')

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user.save()
            messages.success(request, 'User successfully created?')

            return redirect('login')

    return render(request, 'user/signup.html', {'form':form})


def logout(request):
    pass
