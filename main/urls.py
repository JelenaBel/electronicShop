
from django.urls import path
from . import views

urlpatterns = [
    # url and function for main page
    path('', views.index, name='main'),


    path('about', views.about, name='about'),

    # url and function for 'All' page
    path('shop_all', views.shop, name='shop'),
    path('products_category/<category_id>', views.products_category, name='products_category'),

    # url and function for 'Search' page
    path('search_products', views.search_products, name='search_products'),
    path('show_product/<product_id>', views.show_product, name='show_product'),
    path('mobile', views.mobile, name='mobile'),
    path('computers', views.computers, name='computers'),
    path('laptops', views.laptops, name='laptops'),
    path('tv_video', views.tv_video, name='tv_video'),
    path('home_tech', views.home_tech, name='home_tech'),
    path('audio', views.audio, name='audio'),
    path('children', views.children, name='children'),

]
