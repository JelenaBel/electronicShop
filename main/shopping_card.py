from django.contrib import sessions
from Electronicshop import settings
from main.models import Product


# Shopping card class and constructor
class ShoppingCard:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.shopping_card = cart

    # iteration function
    def __iter__(self):
        product_ids = self.shopping_card.keys()
        shopping_card = self.shopping_card.copy()

        products = Product.objects.filter(product_id__in=product_ids)
        for product in products:
            shopping_card[str(product.product_id)]['product_category_name'] = product.category_id.parent_category
            shopping_card[str(product.product_id)]['product_id'] = product.product_id
            shopping_card[str(product.product_id)]['product_name'] = product.name
            shopping_card[str(product.product_id)]['product_image1'] = str(product.image1)
            shopping_card[str(product.product_id)]['product_price'] = product.price

        for item in shopping_card.values():
            item['price'] = int(shopping_card[str(product.product_id)]['product_price'])
            item['total_price'] = int(item['product_price'])*int(item['quantity'])
            yield item

    # function for counting amount of items in the shopping card
    def __len__(self):

        return sum(item['quantity'] for item in self.shopping_card.values())

    # function for adding items in the shopping card (inner function in Shopping class)
    def add_item(self, product_id):
        product_id = product_id
        product = Product.objects.get(pk=product_id)
        product_id = str(product_id)

        if product_id not in self.shopping_card:
            self.shopping_card[product_id] = {'quantity': 1, 'price': product.price}

        else:
            number = self.shopping_card[product_id]['quantity']+1
            self.shopping_card[product_id] = {'quantity': number, 'price': product.price}

        self.save()

    # function to increase amount of the particular product in the card (inner function in Shopping class)
    def plus(self, product_id):
        product_id = str(product_id)
        product = Product.objects.get(pk=product_id)
        number = self.shopping_card[product_id]['quantity']+1

        self.shopping_card[product_id] = {'quantity': number, 'price': product.price}

        self.save()

    # function to decrease amount of the particular product in the card (inner function in Shopping class)
    def minus(self, product_id):
        product_id = str(product_id)
        product = Product.objects.get(pk=product_id)
        if self.shopping_card[product_id]['quantity'] > 1:
            number = self.shopping_card[product_id]['quantity']-1
            self.shopping_card[product_id] = {'quantity': number, 'price': product.price}
        else:
            del self.shopping_card[product_id]

        self.save()

    # function for saving changes in shopping card and whole shopping card in session variable
    def save(self):
        self.session.modified = True

    # function to delete product from the card (inner function in Shopping class)
    def delete(self, product_id):
        product = Product.objects.get(pk=int(product_id))
        del self.shopping_card[product_id]
        self.save()

    # function for counting amount of items in the shopping card
    def count_card_total_items(self):
        total_card_items = 0
        for el in self.shopping_card.values():
            total_card_items = total_card_items + int(el['quantity'])

        return total_card_items

    # function for counting total sum for all the items in the shopping card
    def count_card_total(self):
        total_card = 0
        for el in self.shopping_card.values():
            total_card = total_card + (int(el['product_price'])*int(el['quantity']))

        return total_card

    # clear shopping card (delete all the products from shopping card)
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()






