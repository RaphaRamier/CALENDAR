from django.urls import path
from calendarapp.views import index, new_task, new_event, delete_event, update_event


urlpatterns = [
    path('', index, name='index'),
    path('new_task', new_task, name='new_task'),
    path('new_event', new_event, name='new_event'),
    path('delete_event/<int:event_id>', delete_event, name='delete_event'),
    path('update_event/<int:event_id>', update_event, name='update_event')

]