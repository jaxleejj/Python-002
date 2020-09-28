from django.shortcuts import render
from django.http import HttpResponse
from .models import T1

# Create your views here.

def index(request):
    return HttpResponse("Hello World ! this is test_page")

def show_page(request):

    to_show=T1.objects.all().filter(n_star__gte=3)
    return render(request, 'index.html', locals())


