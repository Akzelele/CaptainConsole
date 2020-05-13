from console.models import Console, Manufacturer
from item.models import Item, ItemImage
from django.shortcuts import get_object_or_404


def build_context():
    return {
        'items': Item.objects.values('id', 'name', 'price', 'console', 'category', 'itemimage'),
        'consoles': Console.objects.all().order_by('name'),
        'manufacturers': Manufacturer.objects.all().order_by('name'),
        'images': ItemImage.objects.values_list().all()
    }


def build_cart_context():
    return {
        'items': Item.objects.all().order_by('id')
    }


def build_item_context(id):
    return {
        'item': get_object_or_404(Item, pk=id),
        'consoles': Console.objects.all().order_by('name'),
        'manufacturers': Manufacturer.objects.all().order_by('name')
    }


def build_console_context(id):
    return {
        'console': get_object_or_404(Console, pk=id),
        'consoles': Console.objects.all().order_by('name'),
        'manufacturers': Manufacturer.objects.all().order_by('name'),
        'items': Item.objects.values('id', 'name', 'price', 'console', 'category', 'itemimage'),
        'images': ItemImage.objects.values_list().all()
    }
