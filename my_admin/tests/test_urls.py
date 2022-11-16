from django.test import SimpleTestCase
from django.urls import reverse, resolve
from my_admin.views import my_admin, add_product_category, show_category, \
    update_category, update_product, add_product, products_admin, products_admin_category, products_by_categories, \
    delete_product, delete_category, categories_admin, all_categories, users_admin
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

    def test_products_admin_url(self):
        url = reverse('products_admin')
        print(resolve(url))
        self.assertEquals(resolve(url).func, products_admin)

    def test_products_by_categories_url(self):
        url = reverse('products_by_categories')
        print(resolve(url))
        self.assertEquals(resolve(url).func, products_by_categories)

    def test_products_admin_category_url(self):
        url = reverse('products_admin_category', args=[78561641])
        print(resolve(url))
        self.assertEquals(resolve(url).func, products_admin_category)

    def test_categories_admin_url(self):
        url = reverse('categories_admin')
        print(resolve(url))
        self.assertEquals(resolve(url).func, categories_admin)

    def test_products_by_categories_url(self):
        url = reverse('products_by_categories')
        print(resolve(url))
        self.assertEquals(resolve(url).func, products_by_categories)

    def test_all_categories_url(self):
        url = reverse('all_categories')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_categories)

    def test_delete_category_url(self):
        url = reverse('delete_category', args=[78561641])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_category)

    def test_delete_product_url(self):
        url = reverse('delete_product', args=[78561641])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_product)

    def test_users_admin_url(self):
        url = reverse('users_admin')
        print(resolve(url))
        self.assertEquals(resolve(url).func, users_admin)






