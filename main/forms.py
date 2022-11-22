from .models import Product, ProductCategory, Customers

from django.forms import ModelForm, TextInput, Textarea, Select, RadioSelect


# Product form (based on the Product table in database), form is used for adding, updating products on the web-page
# ProductForm help to keep consistency of Product object
class ProductForm(ModelForm):

    class Meta:

        model = Product
        fields = ['name', 'price', "category_id", "image1", "image2", "image3",  "main_feature1",
                  "main_feature2", "main_feature3", "anons_eng", "main_description_name1", "main_description1",
                  "main_description_name2", "main_description2", "main_description_name3", "main_description3",
                  "technical_description_name1", "technical_description1", "technical_description_name2",
                  "technical_description2", "technical_description_name3", "technical_description3", "guaranty",
                  "service_center", "size", "size_with_package", "weight", "weight_with_package", "package_include"]

        widgets = {

            "name": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Name"

            }),
            "price": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Price"

            }),
            'category_id':  RadioSelect(attrs={


            }),
            "main_feature1": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "main_feature1"

            }),
            "main_feature2": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "main_feature2"

            }),
            "main_feature3": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "main_feature3"

                }),

            "anons_eng": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Short eng"

            }),

            "main_description_name1": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "main_description_name1"

            }),


            "main_description1": Textarea(attrs={
                "class": "form-control form-control-sm",
                "placeholder":  "main_description1",
                "rows": "4"

            }),
                      "main_description_name2": TextInput(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "main_description_name2"

                      }),

                      "main_description2": Textarea(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "main_description2",
                          "rows": "4"

                      }),
                      "main_description_name3": TextInput(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "main_description_name3"

                      }),

                      "main_description3": Textarea(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "main_description3",
                          "rows": "4"

                      }),
                      "technical_description_name1": TextInput(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "technical_description_name1"

                      }),

                      "technical_description1": Textarea(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "technical_description1",
                          "rows": "4"

                      }),
                      "technical_description_name2": TextInput(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "technical_description_name2"

                      }),

                      "technical_description2": Textarea(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "technical_description2",
                          "rows": "4"

                      }),
                      "technical_description_name3": TextInput(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "technical_description_name3"

                      }),

                      "technical_description3": Textarea(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "technical_description3",
                          "rows": "4"

                      }),

            "guaranty":  TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Guaranty "


            }),
            "service_center":  TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Service Center "

            }),
            "size": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Size"

            }),

                      "size_with_package": TextInput(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "size_with_package"

                      }),

            "weight": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Weight"

            }),
                      "weight_with_package": TextInput(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "weight_with_package"

                      }),


                       "package_include": Textarea(attrs={
                          "class": "form-control form-control-sm",
                          "placeholder": "package_include",
                           "rows": "4"
                       }),





        }


# ProductCategory form (based on the ProductCategory table in database),
# form is used for adding, updating ProductCategories on the web-page (in HTML and functionality)
# ProductCategory Form help to keep consistency of ProductCategory object

class ProductCategoryForm(ModelForm):

    class Meta:

        model = ProductCategory
        fields = ['category_name', "parent_category"]
        widgets = {


            "category_name": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Category name"

            }),
            'parent_category': Select(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Choose parent category"
                # "choices": 'categories_for_select'

            })
        }


# Customer form (based on the Customer table in database),
# form is used for adding additional Customer (User) information needed for make an order in the shop
# Customer Form help to keep consistency of Customer object
class CustomersForm(ModelForm):

    class Meta:

        model = Customers
        fields = ['first_name', 'last_name', 'email', 'phone', 'shipping_address', "shipping_city", 'shipping_zip_code']

        widgets = {
            "first_name": TextInput(attrs={

                "class": "form-control form-control-sm",
                "placeholder": "First name"

            }),
            "last_name": TextInput(attrs={

                "class": "form-control form-control-sm",
                "placeholder": "Last name"

            }),
            "email": TextInput(attrs={

                "class": "form-control form-control-sm",
                "placeholder": "e-mail"

            }),
            "phone": TextInput(attrs={

                "class": "form-control form-control-sm",
                "placeholder": "Phone"

            }),


            "shipping_address": TextInput(attrs={

                "class": "form-control form-control-sm",
                "placeholder": "Shipping address"

            }),
            'shipping_city':  TextInput(attrs={

                "class": "form-control form-control-sm",
                "placeholder": "Shipping city"


            }),

            'shipping_zip_code': TextInput(attrs={
                'name': 'Shipping zip code',
                "class": "form-control form-control-sm",
                "placeholder": "Shipping zip code"


            })
        }
