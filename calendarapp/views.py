from django.shortcuts import render, get_object_or_404, redirect
from calendarapp import models
from django.contrib import messages
from calendarapp.models import *



# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    schedule = FamilyEvent.objects.order_by('user').filter(is_active=True)
    return render(request, 'calendar/index.html')


def task(request):
    pass


