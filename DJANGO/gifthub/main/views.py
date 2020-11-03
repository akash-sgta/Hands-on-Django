from datetime import date
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
# =================================
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Main, Cassarole, Developer
from product.models import Occation, Product
from user.models import User

import hashlib
# Create your views here.

#-------------------------------------------------------------
def get_master_template_data():
    data = dict()
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    return data
#--------------------------------
def get_home_template_data():
    data = get_master()

    scrub = Cassarole.objects.all()
    data['cassarole'] = scrub

    scrub = Occation.objects.all()
    data['occation'] = scrub

    scrub = Product.objects.all()
    data['product'] = scrub

    return data
#--------------------------------
def debug(*args):
    for i in args:
        print(i)
#--------------------------------
def getCookie(request, *args):
    try:
        cookies = list()
        for arg in args:
            cookies.append(request.COOKIES[str(arg)])
    except Exception as ex:
        print(f"GET COOKIE EX : {ex}")
        return 'NULL'
    else:
        return cookies
#--------------------------------
def get_user_authenticate(request):

    try:
        crypt = getCookie(request , 'ucrypt')
        if crypt[0] == 'NULL':
            return False
        else:
            admin_list = User.objects.all()
            flag = False
            for admin in admin_list:
                crypt_check = hashlib.md5(f"{admin.email}-{admin.password}".encode()).hexdigest()
                if crypt[0] == crypt_check:
                    flag = True
                    break
            return flag
    except Exception as ex:
        print(f"GET ADMIN EX : {ex}")
#--------------------------------
check_auth = get_user_authenticate
get_master = get_master_template_data
get_home = get_home_template_data
#-------------------------------------------------------------
def home(request):
    data = get_home()

    if check_auth(request) == True:
        data['is_auth'] = True
        data['user_name'] = getCookie(request, 'user_name')[0].split()[0]


    return render(request, 'front/home.html', data)

def about(request):
    data = get_master()

    if check_auth(request) == True:
        data['is_auth'] = True
        data['user_name'] = getCookie(request, 'user_name')[0].split()[0]

    return render(request, 'front/about.html', data)

def contact(request):
    data = get_master()

    if check_auth(request) == True:
        data['is_auth'] = True
        data['user_name'] = getCookie(request, 'user_name')[0].split()[0]

    scrub = Developer.objects.all()
    data['devs'] = scrub

    return render(request, 'front/contact.html', data)

def developer(request):
    data = get_master()

    if check_auth(request) == True:
        data['is_auth'] = True
        data['user_name'] = getCookie(request, 'user_name')[0].split()[0]

    scrub = Developer.objects.all()
    data['devs'] = scrub

    return render(request, 'front/developer.html', data)

def get_404(request):
    data = get_master()

    return render(request, '404.html', data)