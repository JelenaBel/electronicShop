from .models import Product
from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select


class ProductForm(ModelForm):

    class Meta:

        model = Product
        fields = ['product_id', 'name', 'price', "category", "image1", "image2", "image3",  "anons_fi", "anons_eng",
                  "main_description_fi", "main_description_eng", "guaranty", "service_center", "size", "weight"]
        widgets = {
            "product_id": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Product ID "



            }),
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Name"

            }),
            "price": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Price"

            }),
            'category':  Select(attrs={
                "class": "form-control",
                # "choices": 'categories_for_select'

            }),

            "anons_fi": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Short fi"

            }),
            "anons_eng": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Short eng"

            }),

            "main_description_fi": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description fi"

            }),
            "main_description_eng": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description eng"

            }),
            "guaranty":  TextInput(attrs={
                "class": "form-control",
                "placeholder": "Guaranty "


            }),
            "service_center":  TextInput(attrs={
                "class": "form-control",
                "placeholder": "Service Center "

            }),
            "size": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Size"

            }),
            "weight": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Weight"

            })





        }

