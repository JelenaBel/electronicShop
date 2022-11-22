from .shopping_card import ShoppingCard


def shopping_card(request):
    return {'shopping_card': ShoppingCard(request)}
