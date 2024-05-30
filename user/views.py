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

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout')
    return redirect('loginpage')


@login_required
def edit_weekdays(request):
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


@login_required
def members(request):
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


@login_required
def mail_box(request, filter_type=None):
    username=request.user.username
    outbox=Messages.objects.order_by('timestamp').filter(sender_id=request.user.id).exclude(deleted_by=request.user)
    inbox=Messages.objects.filter(recipients__in=[request.user]).order_by('timestamp').exclude(deleted_by=request.user)

    if filter_type == 'read':
        inbox = inbox.filter(read_by=request.user)
    elif filter_type == 'unread':
        inbox = inbox.exclude(read_by=request.user)

    return render(request, 'user/mail_box.html', {'outbox': outbox, 'username': username, 'inbox': inbox})


@login_required
def send_messages(request):
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


@login_required
def mail_view(request, mail_id):
    mail=Messages.objects.get(pk=mail_id)

    if request.user in mail.read_by.all():
        pass
    else:
        if request.user in mail.recipients.all():
            mail.read_by.add(request.user)
            messages.success(request, 'Message read.')
        else:
            messages.error(request, 'You do not have permission to read this message.')

    username=request.user.username
    return render(request, 'user/mail_view.html', {'username': username, 'mail': mail})


@login_required
def delete_message(request, message_id):
    message=get_object_or_404(Messages, id=message_id)

    if request.user in message.recipients.all() or request.user == message.sender:
        message.deleted_by.add(request.user)
        messages.success(request, 'Message deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this message.')

    return redirect('mail_box')
