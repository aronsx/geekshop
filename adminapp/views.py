from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminapp.forms import AdminShopUserUpdateForm, AdminShopUserCreateForm
from mainapp.models import ProductsCategory


class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SetPageTitleMixin:
    page_title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = self.page_title
        return context


class ShopUserList(SuperUserOnlyMixin, SetPageTitleMixin, ListView):
    model = get_user_model()
    page_title = 'админка/пользователи'


class ShopUserCreateView(SuperUserOnlyMixin, SetPageTitleMixin, CreateView):
    model = get_user_model()
    form_class = AdminShopUserCreateForm
    success_url = reverse_lazy('myadmin:index')


class ShopUserUpdateView(SuperUserOnlyMixin, SetPageTitleMixin, UpdateView):
    model = get_user_model()
    form_class = AdminShopUserUpdateForm
    success_url = reverse_lazy('myadmin:index')
    pk_url_kwarg = 'user_pk'
    page_title = 'админка/пользователи/редактирование'


class ShopUserDeleteView(SuperUserOnlyMixin, SetPageTitleMixin, DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('myadmin:index')
    pk_url_kwarg = 'user_pk'
    page_title = 'админка/пользователи/удаление'


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    context = {
        'page_title': 'админка/категории',
        'object_list': ProductsCategory.objects.all()
    }
    return render(request, 'adminapp/categories.html', context=context)
