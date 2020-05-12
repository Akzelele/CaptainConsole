from console.models import Console, Manufacturer
from item.models import Item
from django.shortcuts import get_object_or_404


def build_context():
    consoles = Console.objects.all().order_by('name')
    manufacturers = Manufacturer.objects.all().order_by('name')
    manufacturer_dict = {}
    for man in manufacturers:
        manufacturer_dict[man.name] = []
    for con in consoles:
        for key in manufacturer_dict:
            if con.manufacturer.name == key:
                manufacturer_dict[key].append([con.id, con.name])
    return {
        'manufacturers': manufacturer_dict
    }


def build_item_context():
    items = [{
        'id': item.id,
        'name': item.name,
        'price': item.price,
        'firstImage': item.itemimage_set.first(),
        'category': item.category
    } for item in Item.objects.all().order_by('name')]
    return {'items': items}


def build_cart_context():
    return {
        'consoles': Console.objects.all().order_by('name'),
        'items': Item.objects.all().order_by('id'),
        'manufacturers': Manufacturer.objects.all().order_by('name')
    }


# def build_item_context(id):
#     return {
#         'item': get_object_or_404(Item, pk=id),
#         'consoles': Console.objects.all().order_by('name'),
#         'manufacturers': Manufacturer.objects.all().order_by('name')
#     }


def build_console_context(id):
    return {
        'console': get_object_or_404(Console, pk=id),
        'consoles': Console.objects.all().order_by('name'),
        'manufacturers': Manufacturer.objects.all().order_by('name'),
        'items': Item.objects.all().order_by('name')
    }
