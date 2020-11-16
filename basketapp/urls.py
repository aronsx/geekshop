import basketapp.views as basketapp

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:pk>', basketapp.add, name='add'),
    path('remove/<int:pk>', basketapp.remove, name='remove'),
]
