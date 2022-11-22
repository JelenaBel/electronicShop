from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # login user url and function
    path('login_user', views.login_user, name='login'),

    # logout user url and function
    path('logout_user', views.logout_user, name='logout'),

    # register user url and function
    path('register_user', views.register_user, name='register_user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
