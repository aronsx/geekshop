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
    visit_date = datetime.datetime.now()
    context = {
        'page_title': 'контакты',
        'visit_date': visit_date,
    }
    return render(request, 'mainapp/contact.html', context)
