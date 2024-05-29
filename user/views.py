from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
from django.urls import reverse
from django.utils.html import format_html

from calendarapp.models import FamilyEvent
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


def birthday(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

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


def edit_weekdays(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

    try:
        personal_date=PersonalDates.objects.get(user=request.user)
    except PersonalDates.DoesNotExist:
        # Redirecionar para a página de cadastro de data de nascimento
        return redirect('birthday')

    if request.method == 'POST':
        form=PersonalDateForm(request.POST, instance=personal_date)

        if form.is_valid():
            form.fields['birthday'].widget=forms.HiddenInput()
            form.save()
            messages.success(request, 'Days successfully changed.')
            return redirect('index')
    else:
        form=PersonalDateForm(instance=personal_date)
        form.fields['birthday'].widget=forms.HiddenInput()

    username=request.user.username
    return render(request, 'user/edit_weekdays.html',
                  {'form': form, 'username': username, 'personal_date': personal_date})


def members(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

    username=request.user.username
    users=User.objects.all()
    user_data=[]

    for user in users:
        try:
            personal_dates=PersonalDates.objects.get(user=user)
            available_days=[]

            if personal_dates.monday:
                available_days.append('Monday')
            if personal_dates.tuesday:
                available_days.append('Tuesday')
            if personal_dates.wednesday:
                available_days.append('Wednesday')
            if personal_dates.thursday:
                available_days.append('Thursday')
            if personal_dates.friday:
                available_days.append('Friday')
            if personal_dates.saturday:
                available_days.append('Saturday')
            if personal_dates.sunday:
                available_days.append('Sunday')

            # Adicionando debug print para verificar os dias disponíveis

            birthday=personal_dates.birthday
            print(f"Available days for {user.username}: {available_days}. Birthday: {birthday}")
        except PersonalDates.DoesNotExist:
            # Se não houver registro de PersonalDates para o usuário
            available_days=[]
            birthday='N/A'

        user_data.append({
            'name': user.username,
            'birthday': birthday,
            'available_days': available_days
        })

        print(user_data)

    return render(request, 'user/members.html',
                  {'user_data': user_data, 'username': username})


def mail_box(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

    if PersonalDates.objects.filter(user_id=request.user).exists:
        pass
    else:
        birthday_url=reverse('birthday')
        messages.error(request, format_html(f'Complete your registration <a href="{birthday_url}">here</a>'))

    username=request.user.username
    mail=Messages.objects.order_by('timestamp').filter(sender_id=request.user.id)
    inbox = Messages.objects.filter(recipients__in=[request.user]).order_by('timestamp')

    return render(request, 'user/mail_box.html', {'mail': mail, 'username': username, 'inbox':inbox})


def send_messages(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

    if request.method == 'POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.sender=request.user
            message.save()
            form.save_m2m()

            messages.success(request, 'Your email has been successfully sent.')
            return redirect('mail_box')
    else:
        form=MessageForm()

    username=request.user.username

    return render(request, 'user/send_messages.html', {'form': form, 'username': username})
