from django.shortcuts import render
from console.models import Console
from helper.context_helper import *


def index(request):
    context = build_context()
    return render(request, 'base.html', context)


def get_console_by_id(request, id):
    return render(request, 'console/single_console.html', build_console_context(id))

def manufacturer_index(request):
    context = build_context()
    return render(request, 'base.html', context)
