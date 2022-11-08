
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('shop_all', views.shop, name='shop'),
    path('search_products', views.search_products, name='search_products'),
    path('show_product/<product_id>', views.show_product, name='show_product'),
    path('mobile', views.mobile, name='mobile'),
    path('computers', views.computers, name='computers'),
    path('laptops', views.laptops, name='laptops'),
    path('tv_video', views.tv_video, name='tv_video'),
    path('home_tech', views.home_tech, name='home_tech'),

]
