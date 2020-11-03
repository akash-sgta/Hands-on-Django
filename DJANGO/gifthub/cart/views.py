from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from main.models import Main, Cassarole
from user.models import User
from product.models import Product, Occation
from .models import Cart

import hashlib

# Create your views here.
# --------------------------------------------------------------------------
def get_master_template_data():
    data = dict()
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    return data
# --------------------------------------
def get_home_template_data():
    data = get_master_template_data()

    scrub = Cassarole.objects.all()
    data['cassarole'] = scrub

    scrub = Occation.objects.all()
    data['occation'] = scrub

    scrub = Product.objects.all()
    data['product'] = scrub

    return data
# --------------------------------------
def getCookie(request, *args):
    try:
        cookies = list()
        for arg in args:
            cookies.append(request.COOKIES[str(arg)])
    except Exception as ex:
        print(f"GET COOKIE EX : {ex}")
        return ['NULL']
    else:
        return cookies
# --------------------------------------
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

# --------------------------------------
get_master = get_master_template_data
get_home = get_home_template_data
check_auth = get_user_authenticate
# --------------------------------------------------------------------------
def add_to_cart(request):
    data = get_master()

    if check_auth(request) == True:
        data['is_auth'] = True
        data['user_name'] = getCookie(request, 'user_name')[0].split()[0]
    else:
        return redirect('user_login')

    try:
        if request.method == 'POST':
            temp = request.POST
            form_data = dict()

            form_data['prod-id'] = temp.get('prod-id')
            form_data['username'], form_data['ucrypt'] = getCookie(request, 'user_name', 'ucrypt')
            
            flag = False
            for i in form_data.keys():
                if form_data[i] == '' or form_data[i] == None:
                    flag = True
                    break
            if flag == True:
                raise Exception('Fields Required')
            else:
                users = User.objects.filter(name = form_data['username'])
                if len(users) == 0:
                    raise Exception('Check Cookie for invalid data')
                else:
                    flag = False
                    for user in users:
                        crypt_check = hashlib.md5(f'{user.email}-{user.password}'.encode()).hexdigest()
                        if form_data['ucrypt'] == crypt_check:
                            user_pk = user.pk
                            flag = True
                            break
                    if flag == True:
                        form = dict()
                        form['user'] = User.objects.get(pk = user_pk)
                        form['product'] = Product.objects.get(pk = form_data['prod-id'])
                        form['quantity'] = 1
                        form['price'] = form['product'].price * form['quantity']

                        cart_ref = Cart(user = form['user'],
                                        product = form['product'],
                                        quantity = form['quantity'],
                                        price = form['price'])
                        cart_ref.save()
                    
    except Exception as ex:
        print("ADD TO CART EX : ", ex)



    return redirect('show_cart')

def show_cart(request):
    data = get_master()

    if check_auth(request) == True:
        data['is_auth'] = True
        full_user_name, ucrypt = getCookie(request, 'user_name', 'ucrypt')
        data['user_name'] = full_user_name.split()[0]

        try:
            user_name = full_user_name
            users = User.objects.filter(name=user_name)

            if len(users) == 0:
                raise Exception('User Not Found')
            else:
                flag = False
                for user in users:
                    crypt_check = hashlib.md5(f'{user.email}-{user.password}'.encode()).hexdigest()
                    if ucrypt == crypt_check:
                        user_ref = user
                        flag = True
                        break
                if flag == True:
                    carts = Cart.objects.filter(user = user_ref)
                    print(carts)
                    print(user_ref)
                    if len(carts) == 0:
                        raise Exception('Cart Not Found')
                    else:
                        data['carts'] = carts
                        
        except Exception as ex:
            print(f"SHOW CART EX: {ex}")

    else:
        return redirect('user_login')

    return render(request, 'front/cart/show_cart.html', data)