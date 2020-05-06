from django.shortcuts import render, get_object_or_404
from console.models import Console, Manufacturer
from helper.context_helper import build_context


def index(request):
    context = build_context()
    return render(request, 'navigation.html', context)


def get_console_by_id(request, id):
    return render(request, 'console/single_console.html', {
        'console': get_object_or_404(Console, pk=id)
    })


def manufacturer_index(request):
    context = build_context()
    return render(request, 'navigation.html', context)
