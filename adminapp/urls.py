import adminapp.views as adminapp

from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
]
