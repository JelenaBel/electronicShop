
from django.urls import path
from . import views

urlpatterns = [
    # url and function for main page
    path('', views.index, name='main'),

    # url and function for about us page
    path('about', views.about, name='about'),

    # url and function for 'All' page, whole shop
    path('shop_all', views.shop, name='shop'),

     # url and function for dynamic 'subcategory' shop pages with products from chosen category
    path('products_category/<category_id>', views.products_category, name='products_category'),

    # url and function for 'Search' page
    path('search_products', views.search_products, name='search_products'),

    # url and function for 'Search' page
    path('show_product/<product_id>', views.show_product, name='show_product'),

    # url and function for shopping card' page
    path('shopping_card', views.shopping_card, name='shopping_card'),

    # url and function for 'add to card' functionality
    path('add_to_card/<product_id>', views.add_to_card, name='add_to_card'),

    # url and function for 'delete item from the card' functionality
    path('delete_item_card/<product_id>', views.delete_item_card, name='delete_item_card'),

    # url and function for 'increase quantity of item in the card' functionality
    path('plus_item_card/<product_id>', views.plus_item_card, name='plus_item_card'),

    # url and function for 'decrease quantity of item in the card' functionality
    path('minus_item_card/<product_id>', views.minus_item_card, name='minus_item_card'),

    # url and function for 'clear card' functionality
    path('clear_card', views.clear_card, name='clear_card'),

   # url and function to order products in the shopping card'
    path('order', views.order, name='order'),

    # url and function to Thank for the order page
    path('thank_order', views.thank_order, name='thank_order'),

    # url and function for 'empty card' page
    path('card_empty', views.card_empty, name='card_empty'),

    # url and function for 'user profile' page
    path('user_personal/<user_id>', views.user_personal, name='user_personal'),

    # urls and functions for base product categories pages (top navigation)
    path('mobile', views.mobile, name='mobile'),
    path('computers', views.computers, name='computers'),
    path('laptops', views.laptops, name='laptops'),
    path('tv_video', views.tv_video, name='tv_video'),
    path('home_tech', views.home_tech, name='home_tech'),
    path('audio', views.audio, name='audio'),
    path('children', views.children, name='children'),


]
