import authapp.views as authapp

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
]
