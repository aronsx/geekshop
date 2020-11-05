import json
import os
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from mainapp.models import ProductsCategory, Product
# from django.conf import settings


def load_from_json(file_name):
    with open(file_name, encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill data in db'

    def handle(self, *args, **options):
        items = load_from_json('mainapp/json/categories.json')
        for item in items:
            ProductsCategory.objects.create(**item)

        items = load_from_json('mainapp/json/products.json')
        for item in items:
            category = ProductsCategory.objects.get(name=item['category'])
            item['category'] = category
            Product.objects.create(**item)

        if not User.objects.filter(username='django').exists():
            User.objects.create_superuser(
                'django', 'django@db.local', 'geekbrains')
