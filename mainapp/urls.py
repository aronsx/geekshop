import mainapp.views as mainapp

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('products/', mainapp.products, name='products'),
    path('contact/', mainapp.contact, name='contact'),
]
