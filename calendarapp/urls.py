from django.urls import path
from calendarapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('new_task', new_task, name='new_task'),
    path('new_event', new_event, name='new_event'),
    path('delete_event/<int:event_id>', delete_event, name='delete_event'),
    path('update_event/<int:event_id>', update_event, name='update_event'),
    path('events', events, name='events'),
    path('tasks', tasks, name='tasks'),
    path('event_detail/<int:event_id>', event_detail, name='event_detail'),
    path('update_task/<int:task_id>', update_task, name='update_task'),
    path('delete_task/<int:task_id>', delete_task, name='delete_task'),


]