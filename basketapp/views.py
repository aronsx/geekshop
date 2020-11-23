from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

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
def add(request, product_pk):
    basket_item, _ = Basket.objects.get_or_create(
        user=request.user,
        product_id=product_pk
    )

    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def set(request, basket_pk, qty):
    if request.is_ajax():
        basket_item = Basket.objects.filter(pk=basket_pk).first()
        if not basket_item:
            return JsonResponse(
                {'status': 'error'},
                status=404)
        if qty <= 0:
            basket_item.delete()
        else:
            basket_item.quantity = qty
            basket_item.save()
        basket = request.user.basket.all()
        context = {
            'basket': basket,
        }
        basket_list = loader.render_to_string(
            'basketapp/includes/inc__basket_list.html',
            context=context,
            request=request
        )
        return JsonResponse({
            'status': 'ok',
            'basket_list': basket_list
        })


@login_required
def remove(request, basket_pk):
    basket_item = get_object_or_404(Basket, pk=basket_pk)
    basket_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
