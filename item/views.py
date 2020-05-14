from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from helper.context_helper import build_context, build_item_context
from item.models import Item, ItemImage
import operator


# Create your views here.
context = build_context()
def index(request):
    global context
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
        item = list(context['items'])
        if sort_filter == '-price':
            items = [{
                'id': x['id'],
                'name': x['name'],
                'price': x['price'],
                'firstImage': str(ItemImage.objects.values_list().filter(item_id=x['id']).first()[1])
            } for x in item]
            items.sort(key=operator.itemgetter('price'), reverse=True)
            return JsonResponse({'data': items})


        else:
            items = [{
                'id': x['id'],
                'name': x['name'],
                'price': x['price'],
                'firstImage': str(ItemImage.objects.values_list().filter(item_id=x['id']).first()[1])
            } for x in item]
            items.sort(key=operator.itemgetter(sort_filter))
            return JsonResponse({'data': items})
    return render(request, 'item/index.html', context)



def get_item_by_id(request, id):
    item_context = build_item_context(id)
    return render(request, 'item/item_details.html', item_context)
