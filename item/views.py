from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from helper.context_helper import build_context, build_item_context
from item.models import Item
import operator

# Create your views here.

def index(request):

    context = build_context()

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.itemimage_set.first().image
        } for x in Item.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': items})

    if 'sort_filter' in request.GET:
        sort_filter = request.GET['sort_filter']

        if sort_filter == 'name':
            items = [{
                'id': context['items'][x]['id'],
                'name': context['items'][x]['name'],
                'price': context['items'][x]['price'],
                'firstImage': context['items'][x]['itemimage']
            } for x in range (len(context['items']))]
            items.sort(key=operator.itemgetter('name'))
            return JsonResponse({'data': items})

        if sort_filter == 'pricelhbtn':
            items = [{
                'id': context['items'][x]['id'],
                'name': context['items'][x]['name'],
                'price': context['items'][x]['price'],
                'firstImage': context['items'][x]['itemimage']
            } for x in range (len(context['items']))]
            items.sort(key=operator.itemgetter('price'))
            return JsonResponse({'data': items})

        if sort_filter == 'pricehlbtn':
            items = [{
                'id': context['items'][x]['id'],
                'name': context['items'][x]['name'],
                'price': context['items'][x]['price'],
                'firstImage': context['items'][x]['itemimage']
            } for x in range (len(context['items']))]
            items.sort(key=operator.itemgetter('price'),reverse=True)
            return JsonResponse({'data': items})

    return render(request, 'item/index.html', context)


def get_item_by_id(request, id):
    item_context = build_item_context(id)
    return render(request, 'item/item_details.html', item_context)


