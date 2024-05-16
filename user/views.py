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

        user = auth.authenticate(
            request,
            username = name,
            password = password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Incorrect username or password', extra_tags='danger')
            return redirect('login')

    return render(request, 'user/login.html', {'form': form})


def signup(request):
    form1 = SignUpForm()
    form2 = PersonalDateForm()

    if request.method == 'POST':
        form1 = SignUpForm(request.POST)
        form2 = PersonalDateForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            if form1['password1'].value() != form1['password2'].value():
                messages.error(request, 'Invalid password')
                return redirect('signup')

            username = form1['username'].value()
            password = form1['password2'].value()
            email = form1['email'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                return redirect('signup')

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            user.save()
            dates = form2.save(commit=False)
            dates.user = user.id
            dates.save()

            messages.success(request, 'User successfully created')

            return redirect('login')

    return render(request, 'user/signup.html', {'form1':form1, 'form2':form2})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout')
    return redirect('login')
