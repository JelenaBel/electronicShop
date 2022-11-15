from django.test import TestCase, Client
from django.urls import reverse
from main.models import Product, ProductCategory
from datetime import datetime
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category1 = ProductCategory(category_id=11111111, category_name='Mobile', parent_category='Main')

        self.category1.save()
        self.product = Product(
            product_id=1,
            name='TEST',
            price='TEST',
            category_id=self.category1,

            main_feature1='TEST',
            main_feature2='TEST',
            main_feature3='TEST',
            anons_eng='TEST',
            main_description_name1='TEST',
            main_description1='TEST',
            main_description_name2='TEST',
            main_description2='TEST',
            main_description_name3='TEST',
            main_description3='TEST',
            technical_description_name1='TEST',
            technical_description1='TEST',
            technical_description_name2='TEST',
            technical_description2='TEST',
            technical_description_name3='TEST',
            technical_description3='TEST',
            guaranty='TEST',
            service_center='TEST',
            size='TEST',
            size_with_package='TEST',
            weight='TEST',
            weight_with_package='TEST',
            package_include='TEST',
            date_added=datetime(2022, 11, 11),
            last_update=datetime(2022, 11, 11)
        )
        self.show_category_url = reverse('show_category', args=[self.category1.category_id])

    def test_show_category_GET(self):
        response = self.client.get(self.show_category_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_category.html')






