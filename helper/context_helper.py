from console.models import Console, Manufacturer
from item.models import Item, ItemImage
from user.models import UserSearchHistory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def build_context():
    manufacturer_dict = build_navbar_context()
    return {
        'items': Item.objects.values('id', 'name', 'price', 'console', 'category', 'itemimage'),
        'manufacturers': manufacturer_dict,
        'images': ItemImage.objects.values_list().all()
    }


def build_navbar_context():
    manufacturers = Manufacturer.objects.all().order_by('name')
    consoles = Console.objects.all().order_by('name')
    manufacturer_dict = {}
    for man in manufacturers:
        manufacturer_dict[man.name] = []
    for con in consoles:
        for key in manufacturer_dict:
            if con.manufacturer.name == key:
                manufacturer_dict[key].append([con.id, con.name])
    return manufacturer_dict


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
    manufacturer_dict = build_navbar_context()
    return {
        'console': get_object_or_404(Console, pk=id),
        'manufacturers': manufacturer_dict,
        'items': Item.objects.values('id', 'name', 'price', 'console', 'category', 'itemimage'),
        'images': ItemImage.objects.values_list().all()
    }

def build_searh_history(currentuser):
    return {
        'search_history': UserSearchHistory.objects.filter(user = currentuser)
    }
