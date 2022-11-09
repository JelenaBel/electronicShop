from django.shortcuts import render
from .models import Product, ProductCategory
from django.core.paginator import Paginator
from django.db.models import Q


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


# Own dynamic (connected to database) product page for each product.
def show_product(request, product_id):

    product = Product.objects.get(pk=product_id)

    return render(request, 'main/show_product.html', {'product': product})


# Mobile category dynamic (connected to database) page with list of products in this category.
# 'Mobile' page html rendering
def mobile(request):
    parent_category = 'mobile'
    sub_categories = ProductCategory.objects.all().filter(parent_category='mobile')
    products = Product.objects.all().filter(Q(category_id__category_name__exact='Mobile')
                                            | Q(category_id__parent_category='mobile'))
    print(len(products))
    pagination = Paginator(Product.objects.filter(Q(category_id__category_name__exact='Mobile')
                                            | Q(category_id__parent_category='mobile')), 8)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/mobile.html', {'sub_categories': sub_categories, 'products': products, 'products_on_page': products_on_page})


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

    return render(request, 'main/computers.html', {'sub_categories': sub_categories,
                                                   'products': products, 'products_on_page': products_on_page})


def home_tech(request):
    sub_categories = ProductCategory.objects.all().filter(parent_category='home')
    products = Product.objects.all().filter(Q(category_id__category_name__exact='Home')
                                            | Q(category_id__parent_category='home'))
    print(len(products))
    pagination = Paginator(Product.objects.filter(Q(category_id__category_name__exact='Home')
                                                  | Q(category_id__parent_category='home')), 8)


    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/home_tech.html', {'sub_categories': sub_categories,
                                                   'products': products, 'products_on_page': products_on_page})


def tv_video(request):
    category = 'tv/video'
    products = Product.objects.filter(category=category)
    pagination = Paginator(Product.objects.filter(category=category), 4)
    page = request.GET.get('page')
    products_on_page = pagination.get_page(page)
    print(len(products))

    return render(request, 'main/tv_video.html', {'products': products, 'products_on_page': products_on_page})


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


