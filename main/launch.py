from main.models import Product, User, ProductCategory, OrderItems, Orders, Customers
import json
from django.db import migrations


class Launch:
    def __init__(self, request):
        self.launched = False
        self.categories = []

    def launch_categories(self):
        with open('main_productcategory.json') as category_file:
            data = json.load(category_file)

        for i in range(0, len(data)):
            product_category = ProductCategory()
            product_category.category_id = data[i]['category_id']
            product_category.category_name = data[i]['category_name']
            product_category.parent_category = data[i]['parent_category']

            self.categories.append(product_category)
        for el in self.categories:
            print(el.category_name)
        return self.categories





