from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import AdminShopUserUpdateForm, AdminShopUserCreateForm, AdminProductCategoryUpdateForm, \
    AdminProductUpdateForm
from mainapp.models import ProductsCategory, Product


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
    return render(request, 'adminapp/categories_list.html', context=context)


class ProductCategoryCreateView(SuperUserOnlyMixin, SetPageTitleMixin, CreateView):
    model = ProductsCategory
    success_url = reverse_lazy('myadmin:categories')
    form_class = AdminProductCategoryUpdateForm
    page_title = 'категории продуктов/создание'


class ProductCategoryUpdateView(SuperUserOnlyMixin, SetPageTitleMixin, UpdateView):
    model = ProductsCategory
    success_url = reverse_lazy('myadmin:categories')
    form_class = AdminProductCategoryUpdateForm
    page_title = 'категории продуктов/редактирование'


@user_passes_test(lambda u: u.is_superuser)
def category_products(request, pk):
    category = get_object_or_404(ProductsCategory, pk=pk)
    object_list = category.product_set.all()
    context = {
        'page_title': f'категория {category.name}/продукты',
        'category': category,
        'object_list': object_list
    }
    return render(request, 'adminapp/category_products_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    category = get_object_or_404(ProductsCategory, pk=pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'myadmin:category_products',
                kwargs={'pk': category.pk}
            ))
    else:
        form = AdminProductUpdateForm(
            initial={
                'category': category,
            }
        )

    context = {
        'page_title': 'продукты/создание',
        'form': form,
        'category': category,
    }
    return render(request, 'adminapp/product_update.html', context)


class ProductDetail(SuperUserOnlyMixin, DetailView):
    model = Product
