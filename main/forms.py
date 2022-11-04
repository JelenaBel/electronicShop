from .models import Product

from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select


class ProductForm(ModelForm):

    class Meta:

        model = Product
        fields = ['name', 'price', "category", "image1", "image2", "image3",  "main_feature1",
                  "main_feature2", "main_feature3", "anons_eng", "main_description_name1", "main_description1",
                  "main_description_name2", "main_description2", "main_description_name3", "main_description3",
                  "technical_description_name1", "technical_description1", "technical_description_name2", "technical_description2",
                  "technical_description_name3", "technical_description3", "guaranty", "service_center", "size",
                  "size_with_package", "weight", "weight_with_package", "package_include"]

        widgets = {

            "name": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Name"

            }),
            "price": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Price"

            }),
            'category':  Select(attrs={
                "class": "form-control form-control-sm",
                # "choices": 'categories_for_select'

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

