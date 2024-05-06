from django.urls import path
from calendarapp.views import index, task, new_event


urlpatterns = [
    path('', index, name='index'),
    path('task', task, name='task'),
    path('new_event/', new_event, name='new_event')

]