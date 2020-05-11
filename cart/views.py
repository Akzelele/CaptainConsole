from django.shortcuts import render
from django.http import JsonResponse
from helper.context_helper import *
from item.models import Item

def index(request):
    context = build_context()
    empty = []
    return render(empty,'cart/user_cart.html',context)


def get_cart(request):
    cart_context = build_cart_context()

    return render(request, 'cart/user_cart.html', cart_context)
