

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('my_admin', views.my_admin, name='my_admin'),
    path('add_product', views.add_product, name='add_product'),
    path('products_admin', views.products_admin, name='products_admin'),
    path('users_admin', views.users_admin, name='users_admin'),
    path('update_product/<product_id>', views.update_product, name='update_product'),
    path('delete_product/<product_id>', views.delete_product, name='delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
