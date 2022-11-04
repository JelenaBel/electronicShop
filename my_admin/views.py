from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Product
from main.forms import ProductForm
import random
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.


def show_product(request, product_id):

    product = Product.objects.get(pk=product_id)

    return render(request, 'main/show_product.html', {'product': product})


def add_product(request):
    submitted = False
    error = ''

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.product_id = random.randint(10000000, 99999999)
            product.save()
            return HttpResponseRedirect('add_product?submitted=True')
    else:
        form = ProductForm
        context = {

            'form': form
        }

        return render(request, 'add_product.html', context)


def my_admin(request):
    products = Product.objects.all()
    products_together = len(products)
    users = User.objects.all()
    users_together = len(users)

    return render(request, 'my_admin.html', {'products_together': products_together, 'users_together': users_together})


def products_admin(request):
    products = Product.objects.all()

    return render(request, 'products_admin.html', {'products': products})


def users_admin(request):
    users = User.objects.all()
    return render(request, 'users_admin.html', {'users': users})


def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products_admin')

    return render(request, 'update_product.html', {'product': product, 'form': form})


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()

    return redirect('products_admin')

# Create your views here.
