from django.shortcuts import render, get_object_or_404
from console.models import Console


# Create your views here.
def index(request):
    context = {'consoles': Console.objects.all().order_by('name')}
    return render(request, 'console/index.html', context)


def get_console_by_id(request, id):
    return render(request, 'console/single_console.html', {
        'console    ': get_object_or_404(Console, pk=id)
    })
