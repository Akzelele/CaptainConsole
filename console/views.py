from django.shortcuts import render
from helper.context_helper import *


def index(request):
    context = build_context()
    return render(request, 'base.html', context)


def get_console_by_id(request, console_id):
    return render(request, 'console/single_console.html', build_console_context(console_id))


def manufacturer_index(request):
    context = build_context()
    return render(request, 'base.html', context)
