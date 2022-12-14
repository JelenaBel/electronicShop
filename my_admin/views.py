from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Product, ProductCategory, Orders, Customers, OrderItems
from main.forms import ProductForm, ProductCategoryForm
from .forms import OrderForm
import random
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.encoding import smart_bytes, force_str
from datetime import datetime


# In this section written is all the functions (views) for the my_admin part

# show_product function (dynamic, info from DB)
def show_product(request, product_id):

    product = Product.objects.get(pk=product_id)

    return render(request, 'main/show_product.html', {'product': product})


# show_category function (dynamic, info from DB)
def show_category(request, category_id):

    category = ProductCategory.objects.all().get(category_id=category_id)
    sub_key = category.category_name.lower()
    sub = ProductCategory.objects.all().filter(parent_category=sub_key)
    return render(request, 'show_category.html', {'category': category, 'sub': sub})


# all categories function for drawing categories tree (dynamic, info from DB)
def all_categories(request):
    categories = {}
    category = ProductCategory.objects.all().filter(parent_category='main')
    for el in category:
        search_key = el.category_name.lower()
        sub = ProductCategory.objects.all().filter(parent_category=search_key)
        categories[el] = sub

    return render(request, 'all_categories.html', {'categories': categories})


# all categories function, (all categories in the table)  (dynamic, info from DB)
def categories_admin(request):
    categories = ProductCategory.objects.all().order_by('parent_category')

    return render(request, 'categories_admin.html', {'categories': categories})


# add category function (save info into DB)
def add_product_category(request):
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


# update category function (save info into DB)
def update_category(request, category_id):
    category = ProductCategory.objects.get(pk=category_id)
    form = ProductCategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('categories_admin')

    return render(request, 'update_category.html', {'category': category, 'form': form})


# delete category function (delete from DB)
def delete_category(request, category_id):
    category = ProductCategory.objects.get(pk=category_id)
    try:
        category.delete()
        messages.success(request, 'Category ' + category.category_name + ' was successfully deleted')
        return redirect('categories_admin')

    except:
        messages.error(request, 'You can not delete Category if any product belong to it. '
                                'Delete all the products in this category first')
        return redirect('categories_admin')


# products divided by categories, easy use for Admin, ergonomic CMS (dynamic, info from DB)
def products_by_categories(request):
    categories = {}
    category = ProductCategory.objects.all().filter(parent_category='main')
    for el in category:
        search_key = el.category_name.lower()
        sub = ProductCategory.objects.all().filter(parent_category=search_key)
        categories[el] = sub

    return render(request, 'products_by_categories.html', {'categories': categories})


# show only products from chosen category (dynamic)
def products_admin_category(request, category_id):
    products = Product.objects.all().filter(category_id=category_id)

    return render(request, 'products_admin_category.html', {'products': products})


# add product functionality (adding new product to DB)
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
            return redirect('products_admin')
    else:
        form = ProductForm
        context = {

            'form': form
        }

        return render(request, 'add_product.html', context)


# my_admin main page/Dashboard  functionality (dynamic, up-to-date info for the diagrams)
def my_admin(request):
    products = Product.objects.all()
    products_together = len(products)
    now = datetime.now()
    day = now.day - 1
    new_products = Product.objects.all().filter(date_added__day=day)
    new_products_number = len(new_products)
    users = User.objects.all()
    users_together = len(users)
    categories = ProductCategory.objects.all()
    categories_together = int(len(categories))

    # creating products in categories bar_chart
    unsorted_info = {}
    categories_names = []
    product_numbers = []
    for el in categories:
        product = Product.objects.filter(category_id=el.category_id)
        unsorted_info[el.category_name] = len(product)

    sort_orders = sorted(unsorted_info.items(), key=lambda x: x[1], reverse=True)
    first_zero= 0
    for i in sort_orders:
        name_cat = force_str(i[0], encoding='utf-8', strings_only=False, errors='strict')
        if int(i[1]) == 0 and first_zero == 0:
            categories_names.append(name_cat)
            product_numbers.append(int(i[1]))
            first_zero = 1
        elif int(i[1]) != 0:
            categories_names.append(name_cat)
            product_numbers.append(int(i[1]))

    barcolors_base = ["red", "green", "blue", "orange", "brown", "pink", "yellow", "lightblue",
                      "orange", "brown", "red", "green", "blue", "orange", "brown",
                      "red", "green", "blue", "orange", "brown",
                      "red", "green", "blue", "orange", "brown"]

    barcolors = barcolors_base[0: len(categories_names)]
    print(categories_names)



# creating best selling products cards

    order_items = OrderItems.objects.all()
    items = {}
    on = False
    for el in order_items:
        for key, val in items.items():
            if el.product_id.product_id == key:
                value = int(el.quantity)+int(val)
                items[key] = value
                on = True

        if not on:
            items[el.product_id.product_id] = el.quantity
        on = False
    sort_items = sorted(items.items(), key=lambda x: int(x[1]), reverse=True)

    final_items = {}
    items_per_category = {}
    sorted_items = dict(sort_items)
    counter = 0
    for avain, arvo in sorted_items.items():
        if counter == 5:
            break

        product = Product.objects.get(pk=avain)

        total = float(product.price)*int(arvo)
        final_items[product] = (arvo, total)
        counter = counter+1


# Creating revenue division chart
    revenue_division = {}
    for prod, info in final_items.items():
        already = False

        if prod.category_id.parent_category == 'main':
            category = prod.category_id.category_name.lower()
        else:
            category = prod.category_id.parent_category.lower()

        for kkk, vvv in revenue_division.items():
            if category == kkk:
                revenue_division[kkk] = int(vvv)+int(info[1])
                already = True
        if not already:
            revenue_division[category] = int(info[1])

    for kkk, vvv in revenue_division.items():
        print(kkk, vvv)

    return render(request, 'my_admin.html', {'products_together': products_together, 'users_together': users_together,
                                             'categories_together': categories_together,
                                             'categories_names': categories_names,
                                             'product_numbers': product_numbers, 'barcolors': barcolors,
                                             'new_products_number': new_products_number, 'final_items': final_items})


# all the products in the shop admin page function (dynamic)
def products_admin(request):
    products = Product.objects.all()

    return render(request, 'products_admin.html', {'products': products})


# all the orders in the my_admin page function (dynamic)
def orders_admin(request):
    orders = Orders.objects.all()

    return render(request, 'orders_admin.html', {'orders': orders})


# show chosen order info in my_admin function
def view_order_admin(request, order_id):
    order = Orders.objects.get(order_id=order_id)
    customer_id = order.customer_id.customer_id
    print("customer id - ", customer_id)

    customer = Customers.objects.get(customer_id=customer_id)
    user = User.objects.get(id=customer.customer_id)
    order_items = OrderItems.objects.filter(order_id__order_id=order_id)
    products = []
    for el in order_items:
        product = Product.objects.get(product_id=el.product_id.product_id)
        products.append(product)

    for qui in products:
        print(qui.name)

    return render(request, 'view_order_admin.html', {'order': order, 'user': user, 'customer': customer,
                                                     'order_items': order_items, 'products': products})


def update_order(request, order_id):
    order = Orders.objects.get(pk=order_id)
    form = OrderForm(request.POST or None, instance=order)
    customer_id = order.customer_id_id
    print("customer id - ", customer_id)
    customer = Customers.objects.get(customer_id=customer_id)

    if form.is_valid():
        updated_order = form.save(commit=False)
        updated_order.order_id = order.order_id
        updated_order.customer_id_id = customer_id
        updated_order.items_total = order.items_total
        updated_order.price_total = order.price_total

        updated_order.save()

        customer.shipping_address = form.cleaned_data['shipping_address']
        customer.shipping_city = form.cleaned_data['shipping_city']
        customer.shipping_zip_code = form.cleaned_data['shipping_zip_code']
        customer.save()
        return redirect('orders_admin')

    return render(request, 'update_order_admin.html', {'order': order, 'form': form})


def delete_order(request, order_id):
    order = Orders.objects.get(pk=order_id)
    order_items_list = OrderItems.objects.filter(order_id=order_id)
    for el in order_items_list:
        el.delete()
    order.delete()
    messages.success(request, 'Order ' + order_id + ' was successfully deleted')
    return redirect('orders_admin')


# search products by name in the admin page function (dynamic)
def products_search_admin(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_products = Product.objects.filter(name__contains=searched)
        return render(request, 'products_search_admin.html', {'searched': searched,
                                                              'searched_products': searched_products})
    else:

        return render(request, 'products_search_admin.html')


# "all the users in the shop" admin page function (dynamic)
def users_admin(request):
    users = User.objects.all()
    return render(request, 'users_admin.html', {'users': users})


# update product functionality (saving product changes to DB), dynamic
def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products_admin')

    return render(request, 'update_product.html', {'product': product, 'form': form})


# delete chosen product functionality (dynamic)
def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    messages.success(request, 'Product ' + product.name + ' was successfully deleted')
    return redirect('products_admin')


