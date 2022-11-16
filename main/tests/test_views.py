from django.test import TestCase, Client
from django.urls import reverse
from main.models import Product, ProductCategory


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_category_products_GET(self):
        category1 = ProductCategory(category_id=11111111, category_name='mobile')
        category1.save()

        sub_category = ProductCategory(category_id=11111121, category_name='mobile Apple',
                                       parent_category=category1.category_name)
        sub_category.save()

        product = Product(
                product_id=1,
                name='TEST',
                price='TEST',
                category_id=category1,
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
                )
        product.save()

        product_category_url = reverse('products_category', args=[category1.category_id])

        response = self.client.get(product_category_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/products_category.html', )


def test_show_product_GET(self):
    category1 = ProductCategory(category_id=11111111, category_name='mobile')
    category1.save()

    sub_category = ProductCategory(category_id=11111121, category_name='mobile Apple',
                                   parent_category=category1.category_name)
    sub_category.save()

    product = Product(
        product_id=1,
        name='TEST',
        price='TEST',
        category_id=category1,
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
    )
    product.save()

    product_category_url = reverse('show_product', args=[product.product_id])

    response = self.client.get(product_category_url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'main/show_product.html', )