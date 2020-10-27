from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home_view(request, *args, **kwargs):
    data = dict()
    from_products = Product.objects.get()
    data['']
    return render(request, 'home.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})