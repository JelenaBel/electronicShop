from django import template
from main.shopping_card import ShoppingCard


register = template.Library()


@register.simple_tag
def mobile():
    return 'mobile'

@register.simple_tag
def computers():
    return 'computers'

@register.simple_tag
def laptops():
    return 'laptops'

@register.simple_tag
def tv_video():
    return 'tv/video'

@register.simple_tag
def home_tech():
    return 'home_tech'

@register.simple_tag
def children():
    return 'children'

@register.simple_tag
def audio():
    return 'audio'

@register.simple_tag
def items_in_card():

    session = request.session
    card = ShoppingCard(request)
    if card:
        total_items = card.count_card_total_items()
        return total_items
    else:
        return '0'
