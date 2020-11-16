from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import Basket


@login_required
def index(request):
    basket = request.user.basket.all()

    context = {
        'page_title': 'корзина',
        'basket': basket,
    }
    return render(request, 'basketapp/index.html', context)


@login_required
def add(request, pk):
    basket_item, _ = Basket.objects.get_or_create(
        user=request.user,
        product_id=pk
    )

    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
