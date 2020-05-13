from django.shortcuts import render
from django.http import JsonResponse
from helper.context_helper import *
from item.models import Item, ItemImage
from django.core.serializers import serialize
from .forms import ContactForm
from django.shortcuts import redirect

def index(request):
    context = build_cart_context()
    return render(request, "cart/user_cart_site.html", context)


def post_item_list(request):
    items = serialize("json", Item.objects.all(), fields=("name", "price"))
    return render(request, "cart/user_cart.html", {"items": items})
    # svona skilar maður öllum objects
    # {'items': items}


def checkout_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']

            print(first_name)
            return redirect('cart/checkout')

    form = ContactForm()
    return render(request, "cart/contactform.html", {'form': form})
