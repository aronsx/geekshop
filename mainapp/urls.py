import mainapp.views as mainapp

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.products, name='products'),
    path('category/<int:category_pk>/', mainapp.category_items, name='category_items'),
    path('contact/', mainapp.contact, name='contact'),
]
