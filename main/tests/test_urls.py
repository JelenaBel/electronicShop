from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import index, products_category, show_product, search_products


class TestUrls(SimpleTestCase):

    def test_main_url(self):
        url = reverse('main')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_search_products_url(self):
        url = reverse('search_products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search_products)

    def test_products_category_url(self):
        url = reverse('products_category', args= ['11111111'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, products_category)

    def test_show_product_url(self):
        url = reverse('show_product', args=['11111111'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, show_product)
