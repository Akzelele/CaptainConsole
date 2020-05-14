from django.shortcuts import render
from django.http import JsonResponse
from helper.context_helper import *
from item.models import Item, ItemImage
from django.core.serializers import serialize
from .forms import ContactForm, PaymentForm
from .models import Order, OrderItem
from item.models import Item
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

    if request.method == 'POST':
        items = request.COOKIES.get('some_cart_key')
        print(items)
        print(type(items))

        item = Item.objects.get(pk=1)
        OrderItem.objects.create(item=item, quantity=2)
        items_id = OrderItem.objects.get(pk=1)
        order_instance = Order.objects.create(first_name=context['contact_info']['first_name'],
                                              last_name=context['contact_info']['last_name'],
                                              email=context['contact_info']['email'],
                                              country=context['contact_info']['country'],
                                              street_name=context['contact_info']['street_name'],
                                              house_number=context['contact_info']['house_number'],
                                              city=context['contact_info']['city'],
                                              zip=context['contact_info']['zip'],
                                              items=items_id)
        return redirect('item-index')

    return render(request, 'cart/review.html', context)
