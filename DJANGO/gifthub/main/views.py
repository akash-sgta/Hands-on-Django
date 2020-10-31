from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
# =================================
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Main, Cassarole, Developer
from product.models import Occation, Product

# Create your views here.

def home(request):
    data = dict()
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    scrub = Cassarole.objects.all()
    data['cassarole'] = scrub

    scrub = Occation.objects.all()
    data['occation'] = scrub

    scrub = Product.objects.all()
    data['product'] = scrub

    return render(request, 'front/home.html', data)

def about(request):
    data = dict()
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    return render(request, 'front/about.html', data)

def contact(request):
    data = dict()
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    scrub = Developer.objects.all()
    data['devs'] = scrub

    return render(request, 'front/contact.html', data)

def developer(request):
    data = dict()
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    scrub = Developer.objects.all()
    data['devs'] = scrub

    return render(request, 'front/developer.html', data)