from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='basketрим')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField('количество', default=0)
    add_datetime = models.DateTimeField('время', auto_now_add=True)