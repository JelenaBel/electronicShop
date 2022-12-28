from main.models import Orders

from django.forms import ModelForm, TextInput, Textarea, Select, RadioSelect


class OrderForm(ModelForm):

    class Meta:

        model = Orders

        fields = [ 'status', "payment", 'type_of_delivery',
                  'shipping_address', 'shipping_city', 'shipping_zip_code', 'order_date']
        widgets = {


            "status": Select(attrs={
                "class": "form-control form-control-sm",


            }),


            'payment': Select(attrs={
                "class": "form-control form-control-sm",



            }),
            'type_of_delivery': Select(attrs={
                "class": "form-control form-control-sm",

            }),
            "shipping_address": TextInput(attrs={
                "class": "form-control form-control-sm",


            }),
            "shipping_city": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Category name"

            }),
            "shipping_zip_code": TextInput(attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Category name"

            })
        }