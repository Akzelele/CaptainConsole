from django.shortcuts import render
from item.models import Item


# Create your views here.
def index(request):
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'item/index.html', context)
