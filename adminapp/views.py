from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminapp.forms import AdminShopUserUpdateForm, AdminShopUserCreateForm
from mainapp.models import ProductsCategory


class ShopUserList(ListView):
    model = get_user_model()


class ShopUserCreateView(CreateView):
    model = get_user_model()
    form_class = AdminShopUserCreateForm
    success_url = reverse_lazy('myadmin:index')


class ShopUserUpdateView(UpdateView):
    model = get_user_model()
    form_class = AdminShopUserUpdateForm
    success_url = reverse_lazy('myadmin:index')
    pk_url_kwarg = 'user_pk'


class ShopUserDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('myadmin:index')
    pk_url_kwarg = 'user_pk'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    context = {
        'page_title': 'админка/категории',
        'object_list': ProductsCategory.objects.all()
    }
    return render(request, 'adminapp/categories.html', context=context)
