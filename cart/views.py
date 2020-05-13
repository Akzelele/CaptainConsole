from django.shortcuts import render
from django.http import JsonResponse
from helper.context_helper import *
from item.models import Item, ItemImage
from django.core.serializers import serialize
from .forms import ContactForm, PaymentForm
from django.shortcuts import redirect


def index(request):
    context = build_cart_context()
    return render(request, "cart/user_cart_site.html", context)


def post_item_list(request):
    items = serialize("json", Item.objects.all(), fields=("name", "price"))
    return render(request, "cart/user_cart.html", {"items": items})
    # svona skilar maður öllum objects
    # {'items': items}


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            request.session['contact_info'] = form.data
            return redirect(payment_view)
    else:
        form = ContactForm()
    return render(request, 'cart/contactform.html', {'form': form})


def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            request.session['payment_info'] = form.data
            return redirect(review_view)
    else:
        form = PaymentForm()
    return render(request, 'cart/paymentform.html', {'form': form})


def review_view(request):
    context = {
        'contact_info': request.session['contact_info'],
        'payment_info': request.session['payment_info']}
    return render(request, 'cart/review.html', context)
