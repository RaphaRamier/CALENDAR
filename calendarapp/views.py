from django.shortcuts import render, get_object_or_404, redirect
from calendarapp import models
from django.contrib import messages
from django.utils.html import format_html
from django.urls import reverse
from calendarapp.models import *
from calendarapp.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime



# Create your views here.
def index(request):

    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

    if PersonalDates.objects.filter(user_id=request.user).exists:
        pass
    else:
        birthday_url = reverse('birthday')
        messages.error(request, format_html(f'Complete your registration <a href="{birthday_url}">here</a>'))

    username = request.user.username
    events = FamilyEvent.objects.order_by('user').filter(is_active=True, user=request.user.id)

    tasks = Task.objects.order_by('user').filter(is_active=True, user=request.user.id)
    return render(request, 'calendar/index.html', {'events': events, 'username':username, 'tasks':tasks})


def events(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

    if PersonalDates.objects.filter(user_id=request.user).exists:
        pass
    else:
        birthday_url=reverse('birthday')
        messages.error(request, format_html(f'Complete your registration <a href="{birthday_url}">here</a>'))

    username=request.user.username
    events=FamilyEvent.objects.order_by('user').filter(is_active=True, user=request.user.id)

    return render(request, 'calendar/events.html', {'events': events, 'username': username})

def tasks(request):

    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

    if PersonalDates.objects.filter(user_id=request.user).exists:
        pass
    else:
        birthday_url = reverse('birthday')
        messages.error(request, format_html(f'Complete your registration <a href="{birthday_url}">here</a>'))

    username = request.user.username
    tasks = Task.objects.order_by('user').filter(user_id=request.user.id)

    return render(request, 'calendar/tasks.html', {'tasks': tasks, 'username':username})

def new_task(request):

    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

    if request.method == 'POST':
        if request.user.is_superuser:
            form = CreateAdminTaskForm(request.POST)
        else:
            form = CreateTaskForm(request.POST)

        user=User.objects.get(id=request.user.id)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            messages.success(request, 'Task successfully created')
            return redirect('index')
    else:
        if request.user.is_superuser:
            form=CreateAdminTaskForm()
        else:
            form=CreateTaskForm()

    username=request.user.username

    return render(request, 'calendar/new_task.html', {'form': form, 'username':username})


def new_event(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')
    username = request.user.username
    form = CreateEventForm()

    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        user = User.objects.get(id=request.user.id)

    if not request.user.is_authenticated:
        messages.error(request, 'To perform this action, user must be logged')
        return redirect('loginpagepage')


    if form.is_valid():

        if form['start_at'].value() > form['end_at'].value():
            messages.error(request, "Event cannot starts after it's end")
            return redirect('new_event')
        event = form.save(commit=False)
        event.user = user
        event.save()
        messages.success(request, 'Event successfully created')
        return redirect('index')

    return render(request, 'calendar/new_event.html', {'form':form, 'username':username})




def delete_event(request, event_id):
    event = FamilyEvent.objects.get(pk=event_id)
    if request.user == event.user:
        event.delete()
        messages.success(request, 'Event deleted!')
        return redirect('index')
    else:
        messages.error(request, "You aren't authorized to delete this event!")
        return redirect('index')


def update_event(request, event_id):
    event = get_object_or_404(FamilyEvent, pk=event_id)


    if request.method == 'POST':
        form=CreateEventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            messages.success(request, 'Event successfully updated.')
            return redirect('index')
    else:
        form=CreateEventForm(instance=event)



    username=request.user.username
    return render(request, 'calendar/update_event.html', {'form': form, 'username': username, 'event': event})

def event_detail(request, event_id):
    event=FamilyEvent.objects.get(pk=event_id)

    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('loginpage')

    if request.user == event.user:

        if PersonalDates.objects.filter(user_id=request.user).exists:
            pass
        else:
            birthday_url=reverse('birthday')
            messages.error(request, format_html(f'Complete your registration <a href="{birthday_url}">here</a>'))

    else:
         messages.error(request, "You aren't authorized to delete this event!")
         return redirect('index')

    username=request.user.username
    tasks = Task.objects.filter(event_id=event_id, user_id=request.user.id)

    return render(request, 'calendar/event_detail.html', {'event': event, 'username': username, 'tasks':tasks})


def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)


    if request.method == 'POST':
        form=CreateTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task successfully updated.')
            return redirect('index')
    else:
        form=CreateTaskForm(instance=task)



    username=request.user.username
    return render(request, 'calendar/update_task.html', {'form': form, 'username': username, 'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.user == task.user:
        task.delete()
        messages.success(request, 'Task deleted!')
        return redirect('index')
    else:
        messages.error(request, "You aren't authorized to delete this task!")
        return redirect('index')