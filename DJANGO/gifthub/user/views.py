from django.http import request
from django.http import response
from django.shortcuts import redirect, render
from django.contrib import messages


from .models import Order, User
from main.models import Main, Cassarole
from product.models import Occation
from cart.models import Cart
from admins.models import Admin

from main.views import get_master_template_data as gmtd
from main.views import get_home_template_data as ghtd

import hashlib
# Create your views here.
# ------------------------------------------------------------------------------
def debug(*args):
    for i in args:
        print(i)
# ----------------------------------
def setCookie(request, *args, **kwargs):
    
    key_list = list(kwargs.keys())
    try:
        if(('file_path' in key_list) and ('data' in key_list)):
            response = render(request, kwargs['file_path'], kwargs['data'])
            for item in key_list:
                if item != 'file_path' and item != 'data':
                    response.set_cookie(f"{item}", kwargs[item])
                    if item == 'ucrypt':
                        response.set_cookie('user_name', kwargs['user_name'])

        else:
            raise Exception('Check arguments passed !')
    except Exception as ex:
        print(f"SET COOKIE EX : {ex}")
    else:
        return response
# ----------------------------------
def getCookie(request, *args):
    try:
        cookies = list()
        for arg in args:
            cookies.append(request.COOKIES[str(arg)])
    except Exception as ex:
        print(f"GET COOKIE EX : {ex}")
        cookies.append(None)
        return cookies
    else:
        return cookies
# ----------------------------------
def set_user_authenticate(*args, **kwargs):
    keys = kwargs.keys()
    try:
        if('email' in keys and 'password' in keys):
            admin = User.objects.get(email=kwargs['email'])
            if kwargs['email'] == admin.email and kwargs['password'] == admin.password:
                return True,admin.name
            else:
                return False,''
        else:
            raise Exception('Check arguments passed !')
    except Exception as ex:
        print(f"SET USER EX : {ex}")
# ----------------------------------
def reset_user_authenticate(request, *args, **kwargs):
    
    key_list = list(kwargs.keys())
    try:
        if(('file_path' in key_list) and ('data' in key_list)):
            response = render(request, kwargs['file_path'], kwargs['data'])
            response.delete_cookie('user_name')
            response.delete_cookie('ucrypt')
        else:
            raise Exception('Check arguments passed !')
    except Exception as ex:
        print(f"RESET ADMIN EX : {ex}")
    else:
        return response
# ----------------------------------
def get_user_authenticate(request):

    try:
        crypt = getCookie(request , 'ucrypt')[0]
        u_name = getCookie(request, 'user_name')[0]
        if crypt == None:
            return False
        else:
            user_list = User.objects.filter(name=u_name)
            flag = False
            if len(user_list) == 0:
                return flag
            else:
                for user in user_list:
                    crypt_check = hashlib.md5(f"{user.email}-{user.password}".encode()).hexdigest()
                    if crypt == crypt_check:
                        flag = True
                        break
                return flag
    except Exception as ex:
        print(f"GET ADMIN EX : {ex}")
# ----------------------------------
def get_admin_authenticate(request):

    try:
        crypt = getCookie(request , 'crypt')
        if crypt[0] == None:
            return False
        else:
            admin_list = Admin.objects.all()
            flag = False
            for admin in admin_list:
                crypt_check = hashlib.md5(f"{admin.username}-{admin.password}".encode()).hexdigest()
                if crypt[0] == crypt_check:
                    flag = True
                    break
            return flag
    except Exception as ex:
        print(f"GET ADMIN EX : {ex}")
# ----------------------------------
check_auth = get_user_authenticate
set_auth = set_user_authenticate
reset_auth = reset_user_authenticate
check_admin_auth = get_admin_authenticate
# ------------------------------------------------------------------------------

def user_list(request):

    if check_admin_auth(request) == False:
        return redirect('panel_login')

    data = dict()
    data['page'] = 'users'
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    scrub = User.objects.all().order_by('-pk')
    data['user_detail'] = scrub

    return render(request, 'back/user/show_users.html', data)

def user_login(request):

    data = ghtd()

    if check_auth(request) == True:
        return redirect('home')

    if request.method == 'POST':
        form_data = dict()
        temp = request.POST
        print("\n",temp,"\n")

        try:
            if str(temp.get('ok')) == 'signup':
                form_data['name'] = temp.get('name')
                form_data['email'] = temp.get('email_id')
                form_data['password'] = temp.get('pwd')
                form_data['address'] = temp.get('address')
                form_data['phone'] = temp.get('phone')

                flag = False
                for i in form_data.values():
                    if i == '' or i == None:
                        flag = True
                        break
                if flag == True:
                    data['alert_type'] = 'SIGNUP ERROR'
                    raise Exception("All fields are required !")
                
                users = User.objects.all()
                flag = False
                for i in users:
                    if ((str(form_data['email']).lower() in str(i.email).lower()) or
                    (str(i.email).lower() in str(form_data['email']).lower())):
                        flag = True
                        break
                if flag == True:
                    data['alert_type'] = 'SIGNUP ERROR'
                    raise Exception("Email id already exists !")

                form = User(name=form_data['name'],
                            email=form_data['email'],
                            password=form_data['password'],
                            address=form_data['address'],
                            phone=form_data['phone'])
                form.save()

                return redirect('home')
            
            if str(temp.get('ok')) == 'login':
                form_data['email'] = temp.get('email_id')
                form_data['password'] = temp.get('pwd')

                flag = False
                for i in form_data.values():
                    if i == '' or i == None:
                        flag = True
                        break
                if flag == True:
                    data['alert_type'] = 'LOGIN ERROR'
                    raise Exception("All fields are required !")

                users = User.objects.all()
                flag = 0
                for i in users:
                    if ((str(form_data['email']).lower() in str(i.email).lower()) or
                    (str(i.email).lower() in str(form_data['email']).lower())):
                        flag += 1
                        if (str(form_data['password']) == str(i.password)):
                            flag += 1
                            idd = i.pk
                        break
                if flag == 0:
                    data['alert_type'] = 'LOGIN ERROR'
                    raise Exception("Email not registered !")
                elif flag == 1:
                    data['alert_type'] = 'LOGIN ERROR'
                    raise Exception("Password Incorrect !")
                else:
                    flag = False
                    user = set_auth(email=form_data['email'], password=form_data['password'])
                if user[0] == False:
                    raise Exception('Admin not found or Password incorrect !')
                else:
                    crypt = hashlib.md5(f"{form_data['email']}-{form_data['password']}".encode()).hexdigest()
                    data['user_name'] = user[1].split()[0]
                    data['is_auth'] = True
                    return setCookie(request, file_path='front/home.html', data=data, ucrypt=crypt, user_name=user[1])

        
        except Exception as e:
            data['alert_type'] = 'LOGIN ERROR'
            data['alert_message'] = f"<h1>{e}</h1>"
            messages.info(request, data['alert_message'])
            

    return render(request, 'front/user/login.html', data)

def user_logout(request):

    if check_auth(request) == False:
        return redirect('user_login')
    
    data = ghtd()
    return reset_auth(request, file_path='front/home.html', data=data)

def put_order(request):

    if check_auth(request) == False:
        return redirect('user_login')
    
    data = ghtd()
    try:
        if request.method == 'POST':
            form_data =dict()
            temp = request.POST
            print(temp)
            
            pick = int(temp.get('order_id'))
            order = Order.objects.filter(pk=pick)[0]
            form_data['user'] = order.user
            form_data['product'] = order.product
            form_data['address'] = temp.get('address')
            form_data['phone'] = temp.get('phone')
            form_data['amount'] = temp.get('p_total')

            order.address = form_data['address']
            order.phone = form_data['phone']
            order.amount = form_data['amount']
            order.completed = True
            
            order.product.stock -= int(temp.get('p_quantity'))

            order.product.save()
            order.save()

            cart = Cart.objects.filter(pk = temp.get('cart_id'))
            cart.delete()

            message = '=========================================================\n'
            message += f"Buyer Name : {order.user.name}\n"
            message += f"Buyer Contact : {order.phone}\n"
            message += f"Shipment Address : {order.address}\n"
            message += '=========================================================\n'
            message += f"Product Name : {order.product.name}\n"
            message += f"Product Quantity : {int(temp.get('p_quantity'))}\n"
            message += f"Product Price : {order.product.price}\n"
            message += '=========================================================\n'
            message += f"Total Price : {order.amount}\n"
            message += '=========================================================\n'
            message += 'Thank You,\nEnjoy the occation with the guilt that you made a purchase here u son of a bi**h.\n'
            fast_mail(order.user.email, message)

            return redirect('show_order')
        else:
            return redirect('show_cart')
    except Exception as e:
        print(f"PUT ORDER EX : {e}")
        return redirect('show_cart')

def show_order(request):
    
    if check_auth(request) == False:
        return redirect('user_login')
    
    data = ghtd()
    data['is_auth'] = True
    data['user_name'] = getCookie(request, 'user_name')[0]
    try:
        user_ref = User.objects.get(name=data['user_name'])
        order_list = Order.objects.filter(user=user_ref).order_by('-pk')
        data['orders'] = order_list
        data['user_name'] = data['user_name'].split()[0]
    except Exception as e:
        print(f"SHOW CART EX : {e}")
        return redirect('show_cart')
    else:
        return render(request, 'front/order/show_order.html' ,data)

def fast_mail(email, order):
    try:
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("thesarcasticmoron420@gmail.com", "d0pWrLJlEX1g") 
        message = f'''Subject : GiftHub\n\n\nOrder Successfully Placed\n{order}'''.encode("utf-8")
        s.sendmail("thesarcasticmoron420@gmail.com", email, message) 
        s.quit()
    except Exception as ex:
        print(f"MAIL EX : {ex}")
    else:
        print("MAIL SUCCESS")

def confirm_order(request):
    if check_auth(request) == False:
        return redirect('user_login')
    
    data = ghtd()
    data['is_auth'] = True
    data['user_name'] = getCookie(request, 'user_name')[0]

    try:
        if request.method == 'POST':
            form_data = dict()
            temp = request.POST

            pick = int(temp.get('cart_id'))
            cart = Cart.objects.filter(pk=pick)
            cart = cart[0]

            form_data['user'] = cart.user
            form_data['product'] = cart.product
            form_data['amount'] = cart.price
            form_data['completed'] = False

            order = Order(user = form_data['user'],
                          product = form_data['product'],
                          amount = form_data['amount'],
                          completed = form_data['completed'])
            order.save()

            data['order'] = order
            data['user_name'] = data['user_name'].split()[0]
            data['cart_id'] = pick
            return render(request ,'front/order/order_confirmation.html', data)

        else:
            return redirect('show_cart')
            
    except Exception as e:
        print(f"CONF EX : {e}")
        return redirect('show_cart')

def reset_orders(request):

    if check_admin_auth(request) == True:

        orders = Order.objects.all()
        for order in orders:
            order.delete()
        
        return redirect('panel')
