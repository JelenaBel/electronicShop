from django.contrib import admin
from.models import Product, OrderItems, Orders, Customers
from.models import ProductCategory


# registering the database tables in Django admin part
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(OrderItems)


