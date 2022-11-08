from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Product, ProductCategory
from main.forms import ProductForm, ProductCategoryForm
import random
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.encoding import smart_bytes, force_str
from datetime import datetime


# Create your views here.


def show_product(request, product_id):

    product = Product.objects.get(pk=product_id)

    return render(request, 'main/show_product.html', {'product': product})


def categories_admin(request):
    categories = ProductCategory.objects.all().order_by('parent_category')

    return render(request, 'categories_admin.html', {'categories': categories})


def add_product_category(request, context=None):
    submitted = False
    error = ''

    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            product_category = form.save(commit=False)
            product_category.category_id = random.randint(10000000, 99999999)
            product_category.save()
            messages.success(request, 'Category ' + product_category.category_name + ' was successfully created')
            return redirect('categories_admin')
    else:
        form = ProductCategoryForm
        context = {

            'form': form
        }

        return render(request, 'add_category.html', context)


def update_category(request, category_id):
    category = ProductCategory.objects.get(pk=category_id)
    form = ProductCategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('categories_admin')

    return render(request, 'update_category.html', {'category': category, 'form': form})


def delete_category(request, category_id):
    category = ProductCategory.objects.get(pk=category_id)
    try:
        category.delete()
        messages.success(request, 'Category ' + category.category_name + ' was successfully deleted')
        return redirect('categories_admin')

    except:
        messages.error(request, 'You can not delete Category if any product belong to it. Delete all the products in this category first')
        return redirect('categories_admin')


def add_product(request):
    submitted = False
    error = ''

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.product_id = random.randint(10000000, 99999999)
            product.save()
            messages.success(request, 'Product ' + product.name + ' was successfully added')
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
    categories = ProductCategory.objects.all()
    categories_together = int(len(categories))
    unsorted_info = {}
    categories_names = []
    product_numbers = []
    for el in categories:
        product = Product.objects.all().filter(category_id=el.category_id)
        unsorted_info[el.category_name]=len(product)

    sort_orders = sorted(unsorted_info.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        name_cat = force_str(i[0], encoding='utf-8', strings_only=False, errors='strict')
        categories_names.append(name_cat)
        product_numbers.append(int(i[1]))

    barcolors_base = ["red", "green", "blue", "orange", "brown", "pink", "yellow", "lightblue",
                      "orange", "brown", "red", "green", "blue", "orange", "brown",
                      "red", "green", "blue", "orange", "brown",
                      "red", "green", "blue", "orange", "brown"]

    barcolors = barcolors_base[0: len(categories_names)]
    print(categories_names)
    now = datetime.now()
    day = now.day-1
    new_products = Product.objects.all().filter(date_added__day=day)
    new_products_number=len(new_products)

    return render(request, 'my_admin.html', {'products_together': products_together, 'users_together': users_together,
                                             'categories_together': categories_together,
                                             'categories_names': categories_names,
                                             'product_numbers': product_numbers, 'barcolors': barcolors,
                                             'new_products_number': new_products_number})


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
    messages.success(request, 'Product ' + product.name + ' was successfully deleted')
    return redirect('products_admin')

# Create your views here.