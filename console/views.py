from django.shortcuts import render
from console.models import Console


# Create your views here.
def index(request):
    context = {'consoles': Console.objects.all().order_by('name')}
    return render(request, 'console/index.html', context)
