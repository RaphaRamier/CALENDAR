from django.urls import path
from calendarapp.views import index, new_task, new_event


urlpatterns = [
    path('', index, name='index'),
    path('new_task', new_task, name='new_task'),
    path('new_event/', new_event, name='new_event')

]