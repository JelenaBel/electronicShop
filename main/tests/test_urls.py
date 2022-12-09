from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import index, products_category, show_product, search_products, shop, mobile, computers, laptops
from main.views import tv_video, home_tech, audio, children


class TestUrls(SimpleTestCase):

    def test_main_url(self):
        url = reverse('main')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

        # url and function for main page
    def test_shop_all_url(self):
        url = reverse('shop')
        print(resolve(url))
        self.assertEquals(resolve(url).func, shop)

    def test_mobile_url(self):
        url = reverse('mobile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, mobile)

    def test_computers_url(self):
        url = reverse('computers')
        print(resolve(url))
        self.assertEquals(resolve(url).func, computers)

    def test_laptops_url(self):
        url = reverse('laptops')
        print(resolve(url))
        self.assertEquals(resolve(url).func, laptops)

    def test_tv_video_url(self):
        url = reverse('tv_video')
        print(resolve(url))
        self.assertEquals(resolve(url).func, tv_video)

    def test_home_tech_url(self):
        url = reverse('home_tech')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_tech)

    def test_audio_url(self):
        url = reverse('audio')
        print(resolve(url))
        self.assertEquals(resolve(url).func, audio)

    def test_children_url(self):
        url = reverse('children')
        print(resolve(url))
        self.assertEquals(resolve(url).func, children)


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
