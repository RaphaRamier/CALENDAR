from django.urls import path
from user.views import *


urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', signup, name='singup'),
    path('logout', logout, name='logout')
]
