from django.http import request
from django.shortcuts import render

from .models import Product, Occation
from main.models import Main, Cassarole
# Create your views here.

def detail(request, pk):
    data = dict()
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    scrub = Occation.objects.all()
    data['occation'] = scrub

    try:
        scrub = Product.objects.get(pk=pk)
        data['pr'] = scrub
    except:
        scrub = Cassarole.objects.all()
        data['cassarole'] = scrub

        data['alert_type'] = 'ERROR'
        data['alert_message'] = 'Item does not exist, check picker<br>Rollback !'
        return render(request, 'front/alert/home_like.html', data)


    return render(request, 'front/product/detail.html', data)