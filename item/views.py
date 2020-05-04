from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'candies': Item.objects.all().order_by('name')}
    return render(request, 'candy/index.html', context)