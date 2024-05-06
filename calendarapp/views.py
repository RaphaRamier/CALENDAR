from django.shortcuts import render, get_object_or_404, redirect
from calendarapp import models
from django.contrib import messages
from calendarapp.models import *
from calendarapp.forms import CreateEventForm



# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    schedule = FamilyEvent.objects.order_by('user').filter(is_active=True)
    return render(request, 'calendar/index.html')


def task(request):
    pass


def new_event(request):
    form = CreateEventForm()
    return render(request, 'calendar/new_event.html', {'form':form})




