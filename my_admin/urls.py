from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

# here in URLS and functions for my_admin app in Electronicshop
urlpatterns = [
    # main page and Dashboard url in my_admin part
    path('my_admin', views.my_admin, name='my_admin'),

    # add product url and function
    path('add_product', views.add_product, name='add_product'),

     # add product category url and function
    path('add_product_category', views.add_product_category, name='add_product_category'),

    # products admin url and function (full list of all products)
    path('products_admin', views.products_admin, name='products_admin'),

     # products by categories url and function (full list of all products)
    path('products_by_categories', views.products_by_categories, name='products_by_categories'),

    # admin for chosen category url and function (dynamic)
    path('products_admin_category/<category_id>', views.products_admin_category, name='products_admin_category'),

    # admin categories  url and function (dynamic, full list of categories)
    path('categories_admin', views.categories_admin, name='categories_admin'),

    # admin categories  url and function (dynamic, full list of categories)
    path('all_categories', views.all_categories, name='all_categories'),

    # show chosen category url and rules (dynamic)
    path('show_category/<category_id>', views.show_category, name='show_category'),

    # update chosen category url and rules (dynamic)
    path('update_category/<category_id>', views.update_category, name='update_category'),

    # delete chosen category url and rules (dynamic)
    path('delete_category/<category_id>', views.delete_category, name='delete_category'),

    # admin users  url and function (dynamic, full list of users)
    path('users_admin', views.users_admin, name='users_admin'),

    # update chosen product url and rules (dynamic)
    path('update_product/<product_id>', views.update_product, name='update_product'),

    # delete chosen product url and rules (dynamic)
    path('delete_product/<product_id>', views.delete_product, name='delete_product'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
