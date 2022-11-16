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


