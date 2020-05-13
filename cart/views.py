from django.shortcuts import render
from django.http import JsonResponse
from helper.context_helper import *
from item.models import Item, ItemImage
from django.core.serializers import serialize

def index(request):
    context = build_context()
    return render(request, 'cart/user_cart_site.html', context)

def post_item_list(request):
    items = serialize('json', Item.objects.all(), fields=('name', 'price'));
    return render(request,'cart/user_cart.html', {'items': items})
    #svona skilar maður öllum objects
    #{'items': items}

def checkout_view(request):
    return render(request, 'cart/checkout.html')