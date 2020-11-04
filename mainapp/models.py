from django.db import models

class ProductsCategory(models.Model):
    """product category"""
    name = models.CharField('категория товара', max_length=64)
    description = models.TextField('описание категории', blank=True)
