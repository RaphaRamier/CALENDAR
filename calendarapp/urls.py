from django.urls import path
from calendarapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('task', task, name='task'),

]