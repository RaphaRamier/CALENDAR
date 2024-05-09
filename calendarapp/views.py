from django.shortcuts import render, get_object_or_404, redirect
from calendarapp import models
from django.contrib import messages
from calendarapp.models import *
from calendarapp.forms import *



# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User must be logged in')
        return redirect('login')
    schedule = FamilyEvent.objects.order_by('user').filter(is_active=True)
    return render(request, 'calendar/index.html')


def task(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

    if not request.user.is_authenticated:
        messages.error(request, 'To perform this action, user must be logged')
        return redirect('login')



        name = form['name'].value()
        description = form['description'].value()
        user = User.objects.get(name=form['user'].value())
        even = FamilyEvent.objects.get(name=form['event'].value())

        event = FamilyEvent.objects.create(
            name=name,
            description=description,
            user=user,
            start_at=start,
            end_at=end
        )

        event.save()
        messages.success(request, 'Event successfully created')

    return render(request, 'calendar/new_event.html', {'form': form})


def new_event(request):
    form = CreateEventForm()

    if request.method == 'POST':
        form = CreateEventForm(request.POST)

    if not request.user.is_authenticated:
        messages.error(request, 'To perform this action, user must be logged')
        return redirect('login')


    if form.is_valid():
        if form['start_at'].value() > form['end_at'].value():
            messages.error(request, "Event cannot starts after it's end")
            return redirect('new_event')


        name        = form['name'].value()
        description = form['description'].value()
        user        = User.objects.get(id=form['user'].value())
        start       = form['start_at'].value()
        end         = form['end_at'].value()

        event = FamilyEvent.objects.create(
            name=name,
            description=description,
            user=user,
            start_at=start,
            end_at=end
        )

        event.save()
        messages.success(request, 'Event successfully created')

    return render(request, 'calendar/new_event.html', {'form':form})




