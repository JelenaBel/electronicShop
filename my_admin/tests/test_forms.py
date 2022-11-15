from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from main.forms import ProductCategoryForm, ProductForm
from main.models import ProductCategory
from datetime import datetime
from django.utils import timezone


class TestForms(TestCase):
    def test_ProductCategoryForm_valid_data(self):
        form = ProductCategoryForm(data={
            'category_name': 'Mobile',
            'parent_category': 'main'

        })
        self.assertTrue(form.is_valid())

    def test_ProductCategoryForm_valid_no_data(self):

        form = ProductCategoryForm(data={

        })
        self.assertFalse(form.is_valid())

    def test_ProductCategoryForm_no_parent(self):
        form = ProductCategoryForm(data={
            'category_name': 'Mobile',

        })
        self.assertFalse(form.is_valid())


# ProductForm testing.
    # Test - valid data for form was given

    def test_ProductForm_valid_data(self):
        databases = '__all__'
        category1 = ProductCategory(category_id=11111111, category_name='Mobile', parent_category='Main')
        category1.save()

        form = ProductForm(data={
                              'name': 'TEST',
                              'price': 'TEST',
                              'category_id': category1,
            'image1': None,
        'image2': None,
        'image3' : None,
        'main_feature1' : 'TEST',
                              'main_feature2': 'TEST',
                              'main_feature3': 'TEST',
                              'anons_eng': 'TEST',
                              'main_description_name1': 'TEST',
                                'main_description1': 'TEST',
                                'main_description_name2': 'TEST',
                                'main_description2': 'TEST',
                                'main_description_name3': 'TEST',
                                'main_description3': 'TEST',
                                'technical_description_name1': 'TEST',
                                'technical_description1': 'TEST',
                                'technical_description_name2' : 'TEST',
                                'technical_description2': 'TEST',
                                'technical_description_name3' : 'TEST',
                                'technical_description3' :'TEST',
                                'guaranty' : 'TEST',
                                'service_center' : 'TEST',
                                'size' : 'TEST',
                                'size_with_package' : 'TEST',
                                'weight': 'TEST',
                                'weight_with_package' : 'TEST',
                                'package_include' : 'TEST',


        })
        self.assertTrue(form.is_valid())

    # Testing Product Form (and restrictions from the database model Product).
    # Testcase - submitting product with invalid ForeignKey for field product_category.

    def test_ProductForm_invalid_foreign_key_data(self):
            category1 = ProductCategory(category_id=11111111, category_name='Mobile', parent_category='Main')
            category1.save()

            form = ProductForm(data={
                'name': 'TEST',
                'category_id': 'Mobile',
                'image1': None,
                'image2': None,
                'image3': None,
                'main_feature1': 'TEST',
                'main_feature2': 'TEST',
                'main_feature3': 'TEST',
                'anons_eng': 'TEST',
                'main_description_name1': 'TEST',
                'main_description1': 'TEST',
                'main_description_name2': 'TEST',
                'main_description2': 'TEST',
                'main_description_name3': 'TEST',
                'main_description3': 'TEST',
                'technical_description_name1': 'TEST',
                'technical_description1': 'TEST',
                'technical_description_name2': 'TEST',
                'technical_description2': 'TEST',
                'technical_description_name3': 'TEST',
                'technical_description3': 'TEST',
                'guaranty': 'TEST',
                'service_center': 'TEST',
                'size': 'TEST',
                'size_with_package': 'TEST',
                'weight': 'TEST',
                'weight_with_package': 'TEST',
                'package_include': 'TEST',

            })
            self.assertFalse(form.is_valid())

# Testing Product Form (and restrictions from the database model Product).
# Testcase - submitting product without name.

    def test_ProductForm_no_name_data(self):
        databases = '__all__'
        category1 = ProductCategory(category_id=11111111, category_name='Mobile', parent_category='Main')
        category1.save()

        form = ProductForm(data={

                              'price': 'TEST',
                              'category_id': category1,
                              'image1': None,
                              'image2': None,
                              'image3' : None,
                              'main_feature1' : 'TEST',
                              'main_feature2': 'TEST',
                              'main_feature3': 'TEST',
                              'anons_eng': 'TEST',
                              'main_description_name1': 'TEST',
                              'main_description1': 'TEST',
                              'main_description_name2': 'TEST',
                              'main_description2': 'TEST',
                              'main_description_name3': 'TEST',
                              'main_description3': 'TEST',
                              'technical_description_name1': 'TEST',
                              'technical_description1': 'TEST',
                              'technical_description_name2' : 'TEST',
                              'technical_description2': 'TEST',
                              'technical_description_name3' : 'TEST',
                              'technical_description3' :'TEST',
                              'guaranty' : 'TEST',
                              'service_center' : 'TEST',
                              'size' : 'TEST',
                              'size_with_package' : 'TEST',
                              'weight': 'TEST',
                              'weight_with_package' : 'TEST',
                              'package_include' : 'TEST',


        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
