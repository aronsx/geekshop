import datetime
import os
import json
import random

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from mainapp.models import ProductsCategory, Product


def get_catalog_menu():
    return ProductsCategory.objects.all()


def get_same_products(product):
    return Product.objects.filter(
        category=product.category).exclude(pk=product.pk)


def get_hot_product():
    products = Product.objects.all()
    return random.choice(products)


def get_same_products(product):
    return Product.objects.filter(
        category=product.category).exclude(pk=product.pk)


def index(request):
    context = {
        'page_title': 'главная',
        'catalog_menu': get_catalog_menu(),
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    hot_product = get_hot_product()

    context = {
        'page_title': 'каталог',
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
        'catalog_menu': get_catalog_menu(),
    }
    return render(request, 'mainapp/products.html', context)


def category_items(request, category_pk):
    if category_pk == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=category_pk)

    context = {
        'page_title': 'каталог',
        'catalog_menu': get_catalog_menu(),
        'products': products,
        'category_pk': category_pk,
    }
    return render(request, 'mainapp/category_items.html', context)


def product_page(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    context = {
        'page_title': 'продукт',
        'catalog_menu': get_catalog_menu(),
        'product': product,
        'category_pk': product.category_id,
    }
    return render(request, 'mainapp/product_page.html', context)


def contact(request):
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'adress': 'В пределах МКАД',
        },
        {
            'city': 'Петербург',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'adress': 'В центре',
        },
        {
            'city': 'Казань',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'adress': 'У моста',
        },
    ]
    visit_date = datetime.datetime.now()
    file_path = os.path.join(settings.BASE_DIR, "static", "locations.json")
    with open(file_path) as f:
        locations_file = json.load(f)
    context = {
        'page_title': 'контакты',
        'locations': locations_file,
        'visit_date': visit_date,
        'catalog_menu': get_catalog_menu(),
    }
    return render(request, 'mainapp/contact.html', context)
