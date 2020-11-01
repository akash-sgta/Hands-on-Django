from django.http import request
from django.shortcuts import render

from main.models import Main
from user.models import User
from product.models import Product
from .models import Cart

# Create your views here.

def add_to_cart(request):
    data = dict()

    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.user_id)
        except Exception as e:
            print("EX : ", e)



    return render(request, 'front/cart/show_cart.html')

def show_cart(request):
    data = dict()

    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    return render(request, 'front/cart/show_cart.html', data)