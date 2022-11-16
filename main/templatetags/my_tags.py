from django import template
from main.models import ProductCategory

register = template.Library()


@register.inclusion_tag('main/categories_main.html')
def main_menu_names():
    category_all = ProductCategory.objects.all().filter(category_id='11111111')
    categories = ProductCategory.objects.all().filter(parent_category_id='11111111')

    return {'category_all': category_all, 'categories': categories}

