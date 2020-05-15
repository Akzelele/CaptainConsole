from django.shortcuts import render
from django.http import JsonResponse
from helper.context_helper import *
from item.models import Item, ItemImage
from django.core.serializers import serialize
from .forms import ContactForm, PaymentForm
from .models import Order, OrderItem
from item.models import Item
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    context = build_cart_context()
    return render(request, "cart/user_cart_site.html", context)


def post_item_list(request):
    items = serialize("json", Item.objects.all(), fields=("name", "price"))
    return render(request, "cart/user_cart.html", {"items": items})


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

    pk_list, quant_list = extract_cookies(request)

    if request.method == 'POST':
        # Creates and saves the order:
        order_instance = Order.objects.create(first_name=context['contact_info']['first_name'],
                                              last_name=context['contact_info']['last_name'],
                                              email=context['contact_info']['email'],
                                              country=context['contact_info']['country'],
                                              street_name=context['contact_info']['street_name'],
                                              house_number=context['contact_info']['house_number'],
                                              city=context['contact_info']['city'],
                                              zip=context['contact_info']['zip'])

        # This creates order items the objects
        for i in range(len(pk_list)):
            item = Item.objects.get(pk=pk_list[i])
            order_item_instance = OrderItem.objects.create(item=item,
                                                           quantity=quant_list[i],
                                                           order_id_id=order_instance.pk)

        messages.success(request, f'Purchased successfully!')
        return redirect('item-index')

    return render(request, 'cart/review.html', context)


def extract_cookies(request):
    '''Extracts information from the cookies and returns a string'''

    items = request.COOKIES.get('some_cart_key')
    temp_list = items.split('"')

    pk_list = []
    quant_list = []

    for i in range(len(temp_list)):
        # returns the item primary key in a list
        if 'pk' in temp_list[i]:
            pk_list.append(temp_list[i + 1])

        if 'quantity' in temp_list[i]:
            quant_list.append(temp_list[i + 1])

    for i in range(len(pk_list)):
        pk_list[i] = int(pk_list[i][1::-2])

    for i in range(len(quant_list)):
        quant_list[i] = int(quant_list[i][1::-4])

    return pk_list, quant_list
