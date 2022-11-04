from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Product
from .forms import ProductForm
import random
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def shop(request):

    products = Product.objects.all()
    pagination = Paginator(Product.objects.all(), 12)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/shop.html', {'products': products, 'products_on_page': products_on_page})


def show_product(request, product_id):

    product = Product.objects.get(pk=product_id)

    return render(request, 'main/show_product.html', {'product': product})


def mobile(request):
    category = 'mobile'
    products = Product.objects.filter(category=category)
    pagination = Paginator(Product.objects.filter(category=category), 8)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/mobile.html', {'products': products, 'products_on_page': products_on_page})


def computers(request):
    category = 'computers'
    products = Product.objects.filter(category=category)
    pagination = Paginator(Product.objects.filter(category=category), 8)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/computers.html', {'products': products, 'products_on_page': products_on_page})


def home_tech(request):
    category = 'home'
    products = Product.objects.filter(category=category)
    pagination = Paginator(Product.objects.filter(category=category), 4)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/home_tech.html', {'products': products, 'products_on_page': products_on_page})


def tv_video(request):
    category = 'tv/video'
    products = Product.objects.filter(category=category)
    pagination = Paginator(Product.objects.filter(category=category), 4)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/tv_video.html', {'products': products, 'products_on_page': products_on_page})



def search_products(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_products = Product.objects.filter(name__contains=searched)
        return render(request, 'main/search_products.html', {'searched': searched,
                                                             'searched_products': searched_products})
    else:

        return render(request, 'main/search_products.html')


def about(request):
    return render(request, 'main/aboutus.html')


