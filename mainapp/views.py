import datetime
from django.shortcuts import render


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
    context = {
        'page_title': 'контакты',
        'locations': locations,
        'visit_date': visit_date,
    }
    return render(request, 'mainapp/contact.html', context)
