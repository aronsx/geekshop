from django.db import models

class ProductsCategory(models.Model):
    """product category"""
    name = models.CharField('категория товара', max_length=64)
    description = models.TextField('описание категории', blank=True)

class Product(models.Model):
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    name = models.CharField('товар', max_length=64)
    description = models.TextField('описание', blank=True)
    short_desc = models.CharField('краткое описание', max_length=64, blank=True)
    price = models.DecimalField('цена', max_digits=8, decimal_places=2, default=0, null=True)
    quantity = models.PositiveIntegerField('количество на складе', default=0)
