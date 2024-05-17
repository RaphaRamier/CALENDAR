from django.urls import path
from user.views import *


urlpatterns = [
    path('login', loginpage, name='loginpage'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('birthday', birthday, name='birthday'),
    path('edit_weekdays/<int:week_id>', edit_weekdays, name='edit_weekdays')
]
