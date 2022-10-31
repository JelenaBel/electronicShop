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
    pagination = Paginator(Product.objects.all(), 4)
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
    pagination = Paginator(Product.objects.filter(category=category), 4)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/mobile.html', {'products': products, 'products_on_page': products_on_page})


def computers(request):
    category = 'computers'
    products = Product.objects.filter(category=category)
    pagination = Paginator(Product.objects.filter(category=category), 4)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/computers.html', {'products': products, 'products_on_page': products_on_page})


def tv_video(request):
    category = 'tv/video'
    products = Product.objects.filter(category=category)
    pagination = Paginator(Product.objects.filter(category=category), 4)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/tv_video.html', {'products': products, 'products_on_page': products_on_page})


def add_product(request):
    submitted = False
    error = ''

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_product?submitted=True')
    else:
        form = ProductForm
        context = {

            'form': form
        }

        return render(request, 'main/add_product.html', context)


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


def my_admin(request):
    products = Product.objects.all()

    return render(request, 'main/my_admin.html', {'products': products})


def products_admin(request):
    products = Product.objects.all()

    return render(request, 'main/products_admin.html', {'products': products})


def users_admin(request):
    users = User.objects.all()
    return render(request, 'main/users_admin.html', {'users': users})


def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products_admin')

    return render(request, 'main/update_product.html', {'product': product, 'form': form})


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()

    return redirect('products_admin')
