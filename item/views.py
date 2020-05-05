from django.shortcuts import render
from item.models import Item


# Create your views here.
def index(request):
    context = {'items': Item.objects.all().order_by('id')}
    return render(request, 'item/index.html', context)
