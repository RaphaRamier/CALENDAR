from django.urls import path
from user.views import *


urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout')
]
