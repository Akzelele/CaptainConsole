from console.models import Console, Manufacturer
from item.models import Item


def build_context():
    return {
        'consoles': Console.objects.all().order_by('name'),
        'items': Item.objects.all().order_by('id'),
        'manufacturers': Manufacturer.objects.all().order_by('name'),
            }
