from django.test import SimpleTestCase
from django.urls import reverse, resolve
from my_admin.views import my_admin, add_product_category, show_category, \
    update_category, update_product, add_product
from main.views import show_product


class TestUrls(SimpleTestCase):

    def test_my_admin_url(self):
        url = reverse('my_admin')
        print(resolve(url))
        self.assertEquals(resolve(url).func, my_admin)

    def test_add_product_category_url(self):
        url = reverse('add_product_category')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_product_category)

    def test_update_category_url(self):
        url = reverse('update_category', args=[78561641])
        print(resolve(url))
        self.assertEquals(resolve(url).func, update_category)

    def test_show_category_url(self):
        url = reverse('show_category', args=[78561641])
        print(resolve(url))
        self.assertEquals(resolve(url).func, show_category)


    def test_add_product_url(self):
        url = reverse('add_product')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_product)

    def test_update_product_url(self):
        url = reverse('update_product', args=[78561641])
        print(resolve(url))
        self.assertEquals(resolve(url).func, update_product)

    def test_show_product_url(self):
        url = reverse('show_product', args=[78561641])
        print(resolve(url))
        self.assertEquals(resolve(url).func, show_product)



