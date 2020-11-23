import adminapp.views as adminapp

from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.ShopUserList.as_view(), name='index'),
    path('user/create/', adminapp.ShopUserCreateView.as_view(), name='user_create'),
    path('user/update/<int:user_pk>/', adminapp.ShopUserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:user_pk>/', adminapp.ShopUserDeleteView.as_view(), name='user_delete'),

    path('categories/', adminapp.categories, name='categories'),
]
