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
    path('category/<int:category_pk>/<int:page_num>/', mainapp.category_items, name='category_items_pages'),


    path('product/<int:product_pk>/', mainapp.product_page, name='product_page'),
    path('contact/', mainapp.contact, name='contact'),
]
