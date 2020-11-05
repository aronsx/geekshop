from django.shortcuts import render
from django.contrib import auth

from authapp.forms import ShopUserLoginForm
from django.http import HttpResponseRedirect


def login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
                # return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ShopUserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'authapp/login.html', context)
