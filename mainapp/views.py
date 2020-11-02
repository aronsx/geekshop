import datetime
import os
import json
from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'каталог',
    }
    return render(request, 'mainapp/products.html', context)


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
    }
    return render(request, 'mainapp/contact.html', context)
