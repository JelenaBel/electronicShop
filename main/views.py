from django.shortcuts import render, redirect
from .models import Product, ProductCategory, Orders, OrderItems, User, Customers
from .shopping_card import ShoppingCard
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CustomersForm
import random
from django.contrib import messages
from django.contrib import sessions
from Electronicshop import settings


# Main page rendering function

def index(request):
    return render(request, 'main/index.html')


# All products in the shop function with Pagination. "All" menu page rendering function.

def shop(request):
    sub_categories = ProductCategory.objects.all().filter(parent_category='main')
    products = Product.objects.all()
    pagination = Paginator(Product.objects.all(), 12)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/shop.html', {'sub_categories': sub_categories, 'products': products,
                                              'products_on_page': products_on_page})


# dynamically show shop pages for each sub-category wit the products from database.

def products_category(request, category_id):

    current_category = ProductCategory.objects.get(pk=category_id)
    name = current_category.category_name.lower()

    parent = current_category.parent_category

    sub_categories = ProductCategory.objects.filter(parent_category=name)
    if len(sub_categories) == 0:
        sub_categories = ProductCategory.objects.filter(parent_category=parent)

    products = Product.objects.filter(category_id=category_id)
    print(len(products))
    pagination = Paginator(Product.objects.filter(category_id=category_id), 12)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)

    return render(request, 'main/products_category.html', {'parent': parent, 'sub_categories': sub_categories,
                                                           'products': products,
                                                           'products_on_page': products_on_page,
                                                           'current_category': current_category})


# Own dynamic (connected to database) product page for each product.

def show_product(request, product_id):

    product = Product.objects.get(pk=product_id)

    return render(request, 'main/show_product.html', {'product': product})


# Mobile category dynamic (connected to database) page with list of products in this category.
# 'Mobile' page html rendering
def mobile(request):
    sub_categories = ProductCategory.objects.all().filter(parent_category='mobile')
    products = Product.objects.all().filter(Q(category_id__category_name__exact='Mobile')
                                            | Q(category_id__parent_category='mobile'))
    print(len(products))
    pagination = Paginator(Product.objects.filter(Q(category_id__category_name__exact='Mobile')
                                                  | Q(category_id__parent_category='mobile')), 8)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/mobile.html', {'sub_categories': sub_categories, 'products': products,
                                                'products_on_page': products_on_page})


# Computers category dynamic (connected to database) page with list of products in this category.
# 'Computers' page html rendering
def computers(request):
    sub_categories = ProductCategory.objects.all().filter(parent_category='computers')
    products = Product.objects.all().filter(Q(category_id__category_name__exact='Computers')
                                            | Q(category_id__parent_category='computers'))
    print(len(products))
    pagination = Paginator(Product.objects.filter(Q(category_id__category_name__exact='Computers')
                                                  | Q(category_id__parent_category='computers')), 8)

    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/computers.html', {'sub_categories': sub_categories,
                                                   'products': products, 'products_on_page': products_on_page})


# Laptops category dynamic (connected to database) page with list of products in this category.
# 'Laptops' page html rendering

def laptops(request):
    sub_categories = ProductCategory.objects.all().filter(parent_category='laptops')
    products = Product.objects.all().filter(Q(category_id__category_name__exact='Laptops')
                                            | Q(category_id__parent_category='laptops'))
    print(len(products))
    pagination = Paginator(Product.objects.filter(Q(category_id__category_name__exact='Laptops')
                                                  | Q(category_id__parent_category='laptops')), 8)

    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/laptops.html', {'sub_categories': sub_categories,
                                                   'products': products, 'products_on_page': products_on_page})


# Home-tech category dynamic (connected to database) page with list of products in this category.
# 'Home-tech' page html rendering

def home_tech(request):
    sub_categories = ProductCategory.objects.all().filter(parent_category='home tech')
    products = Product.objects.all().filter(Q(category_id__category_name__exact='Home tech')
                                            | Q(category_id__parent_category='home tech'))
    print(len(products))
    pagination = Paginator(Product.objects.filter(Q(category_id__category_name__exact='Home tech')
                                                  | Q(category_id__parent_category='home tech')), 8)

    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/home_tech.html', {'sub_categories': sub_categories,
                                                   'products': products, 'products_on_page': products_on_page})


# Tv_video category dynamic (connected to database) page with list of products in this category.
# 'Tv_video' page html rendering

def tv_video(request):
    sub_categories = ProductCategory.objects.all().filter(parent_category='tv/video')
    products = Product.objects.all().filter(Q(category_id__category_name__exact='TV/Video')
                                            | Q(category_id__parent_category='tv/video'))
    print(len(products))
    pagination = Paginator(Product.objects.filter(Q(category_id__category_name__exact='TV/Video')
                                                  | Q(category_id__parent_category='tv/video')), 8)

    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/tv_video.html', {'sub_categories': sub_categories,
                                                  'products': products, 'products_on_page': products_on_page})


# Children category dynamic (connected to database) page with list of products in this category.
# 'Children' page html rendering

def children(request):
    sub_categories = ProductCategory.objects.all().filter(parent_category='children')
    products = Product.objects.all().filter(Q(category_id__category_name__exact='Children')
                                            | Q(category_id__parent_category='children'))
    print(len(products))
    pagination = Paginator(Product.objects.filter(Q(category_id__category_name__exact='Children')
                                                  | Q(category_id__parent_category='children')), 8)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/children.html', {'sub_categories': sub_categories, 'products': products,
                                                'products_on_page': products_on_page})


# Audio category dynamic (connected to database) page with list of products in this category.
# 'Audio' page html rendering
def audio(request):
    sub_categories = ProductCategory.objects.all().filter(parent_category='audio')
    products = Product.objects.all().filter(Q(category_id__category_name__exact='Audio')
                                            | Q(category_id__parent_category='audio'))
    print(len(products))
    pagination = Paginator(Product.objects.filter(Q(category_id__category_name__exact='Audio')
                                                  | Q(category_id__parent_category='audio')), 8)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/audio.html', {'sub_categories': sub_categories, 'products': products,
                                               'products_on_page': products_on_page})


# Search field functionality.
# Search works with all products with Products table in database (searched by product_name).

def search_products(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_products = Product.objects.filter(name__contains=searched)
        return render(request, 'main/search_products.html', {'searched': searched,
                                                             'searched_products': searched_products})
    else:

        return render(request, 'main/search_products.html')


# Rendering AboutUs Page.
def about(request):
    return render(request, 'main/aboutus.html')


# Page for the empty card
def card_empty(request):
    return render(request, 'main/card_empty.html')


# Shopping card  page, with products in shopping card, price, quantity, total sum, alv.
def shopping_card(request):
    card = ShoppingCard(request)
    total_items = card.count_card_total_items()
    print(total_items)
    if total_items > 0:
        total = 0
        for el in card:
            total = total + el['total_price']

        alv = total*0.24
        alv = round(alv, 2)
        return render(request, 'main/shopping_card.html', {'card': card, 'total_items': total_items, 'total': total, 'alv': alv})
    else:
        return render(request, 'main/card_empty.html')


# Add to card functionality. Allows add products to the shopping card.
def add_to_card(request, product_id):
    card = ShoppingCard(request)
    product = Product.objects.get(pk=product_id)
    card.add_item(product_id)

    return redirect('shopping_card')


# delete product from the shopping card
def delete_item_card(request, product_id):
    card = ShoppingCard(request)
    product = Product.objects.get(pk=int(product_id))
    card.delete(product_id)

    return redirect('shopping_card')


# increase amount of certain product in the shopping card functionality.
def plus_item_card(request, product_id):
    card = ShoppingCard(request)
    card.plus(product_id)
    return redirect('shopping_card')


# decrease amount of certain product in the shopping card functionality.
def minus_item_card(request, product_id):
    card = ShoppingCard(request)
    card.minus(product_id)
    return redirect('shopping_card')


# delete all products from the shopping card, clear card.
def clear_card(request):
    card = ShoppingCard(request)
    card.clear()
    return redirect('shopping_card')


# submitting and processing order from the shopping card, add items and order to the database,
# add additional info to the customer profile in the database.
def order(request):
    submitted = False
    error = ''
    session = request.session

    if request.method == 'POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            card = ShoppingCard(request)
            # adding info to customer
            uid = session.get('_auth_user_id')
            user = User.objects.get(pk=uid)
            print('User_id', uid)
            full_customer = Customers.objects.filter(pk=user.id)
            full_customer = form.save(commit=False)
            full_customer.customer_id = user.id
            full_customer.save()

            # adding new order to database
            new_order = Orders()
            new_order.order_id = random.randint(10000000, 99999999)
            new_order.customer_id = full_customer
            total = 0
            for el in card:
                total = total + el['total_price']
            print ('total_price', total)
            new_order.items_total = card.count_card_total_items()
            new_order.price_total = total
            new_order.status = 'new'
            new_order.payment = 'paid'
            new_order.shipping_address = form.cleaned_data['shipping_address']
            new_order.shipping_city = form.cleaned_data['shipping_city']
            new_order.shipping_zip_code = form.cleaned_data['shipping_zip_code']
            new_order.save()

            # adding Items in the shopping cart in to OrderItems table (connected to order)

            for el in card:
                id = el['product_id']
                product = Product.objects.get(pk=id)
                item = OrderItems()
                item.order_id = new_order
                item.product_id = product
                item.quantity = el['quantity']
                item.price = el['price']
                item.total_price = item.quantity*item.price
                item.save()

            card.clear()
        return redirect('thank_order')

    else:
        form = CustomersForm
        context = {

            'form': form
        }

        return render(request, 'main/order.html', context)


# thank for the order page
def thank_order(request):
    return render(request, 'main/thank_order.html')


# user own page with user info and orders, which this user made
def user_personal(request, user_id):
    user = User.objects.get(pk=user_id)
    customer = Customers.objects.get(email=user.email)
    orders = Orders.objects.filter(customer_id__customer_id=customer.customer_id)
    order_items = []
    product = {}
    for el in orders:
        items = OrderItems.objects.filter(order_id__order_id=el.order_id)
        for key in items:
            order_items.append(key)
            product[key.product_id.product_id] = {'product_name': key.product_id.name,
                                                  'product_image1': key.product_id.image1}

    return render(request, 'main/user_personal.html', {'user': user, 'customer': customer, 'orders': orders,
                                                       'order_items': order_items, 'product': product})