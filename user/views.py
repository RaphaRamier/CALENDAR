from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
from user.forms import *


# Create your views here.


def loginpage(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            name=form['username'].value()
            password=form['password'].value()

        user=auth.authenticate(
            request,
            username=name,
            password=password
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
    if request.method == 'POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            if form['password1'].value() != form['password2'].value():
                messages.error(request, 'Invalid password')
                return redirect('signup')

            username=form['username'].value()
            password=form['password2'].value()
            email=form['email'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                return redirect('signup')

            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            user.save()

            loginuser=authenticate(username=username, password=password)

            if loginuser is not None:
                login(request, loginuser)

            messages.success(request, 'Complete the registration.')

            return redirect('birthday')

    else:
        form=SignUpForm()

    return render(request, 'user/signup.html', {'form': form})


@login_required
def birthday(request):
    if request.method == 'POST':
        form=PersonalDateForm(request.POST)
        if form.is_valid():
            if PersonalDates.objects.filter(user_id=request.user.id).exists():
                messages.error(request, 'Birthday already informed')
                return redirect('index')

            dates=form.save(commit=False)
            dates.user=request.user
            dates.save()
            messages.success(request, 'Registration complete.')
            return redirect('index')
    else:
        form=PersonalDateForm()

    username=request.user.username
    return render(request, 'user/birthday.html', {'form': form, 'username': username})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout')
    return redirect('loginpage')


def edit_weekdays(request, week_id):
    personal_date = get_object_or_404(PersonalDates, user=request.user, pk=week_id)

    if request.method == 'POST':
        form=PersonalDateForm(request.POST, instance=personal_date)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=PersonalDateForm(instance=personal_date)

    username=request.user.username
    return render(request, 'user/edit_weekdays.html', {'form': form, 'username': username, 'personal_date':personal_date})
