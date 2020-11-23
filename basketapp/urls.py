import basketapp.views as basketapp

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:product_pk>', basketapp.add, name='add'),
    path('remove/<int:basket_pk>', basketapp.remove, name='remove'),
    path('set/<int:basket_pk>/<int:qty>/', basketapp.set, name='set'),
]
