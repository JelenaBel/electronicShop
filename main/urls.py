
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('shop_all', views.shop, name='shop'),
    path('add_product', views.add_product, name='add_product'),
    path('search_products', views.search_products, name='search_products'),
    path('show_product/<product_id>', views.show_product, name='show_product'),
    path('mobile', views.mobile, name='mobile'),
    path('computers', views.computers, name='computers'),
    path('tv_video', views.tv_video, name='tv_video'),
    path('my_admin', views.my_admin, name='my_admin'),
    path('products_admin', views.products_admin, name='products_admin'),
    path('users_admin', views.users_admin, name='users_admin'),
]
