from datetime import date
from django.http import request
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages

from main.models import Main
from .models import Admin

import hashlib

# Create your views here.

#-----------------------------------------------------------------
def get_master_template_data():
    data = dict()
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    return data
#-------------------------------
def debug(*args):
    for i in args:
        print(i)
#-------------------------------
def setCookie(request, *args, **kwargs):
    
    key_list = list(kwargs.keys())
    try:
        if(('file_path' in key_list) and ('data' in key_list)):
            response = render(request, kwargs['file_path'], kwargs['data'])
            for item in key_list:
                if item != 'file_path' and item != 'data':
                    response.set_cookie(f"{item}", kwargs[item])
                    if item == 'crypt':
                        response.set_cookie('admin_name', kwargs['admin_name'])
        else:
            raise Exception('Check arguments passed !')
    except Exception as ex:
        print(f"SET COOKIE EX : {ex}")
    else:
        return response
#-------------------------------
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
#-------------------------------
def set_admin_authenticate(*args, **kwargs):
    keys = kwargs.keys()
    try:
        if('username' in keys and 'password' in keys):
            admin = Admin.objects.get(username=kwargs['username'])
            if kwargs['username'] == admin.username and kwargs['password'] == admin.password:
                print("HERE")
                return True,admin.name
            else:
                print("THERE")
                return False,''
        else:
            raise Exception('Check arguments passed !')
    except Exception as ex:
        print(f"SET ADMIN EX : {ex}")
#-------------------------------
def reset_admin_authenticate(request, *args, **kwargs):
    
    key_list = list(kwargs.keys())
    try:
        if(('file_path' in key_list) and ('data' in key_list)):
            response = render(request, kwargs['file_path'], kwargs['data'])
            response.delete_cookie('admin_name')
            response.delete_cookie('crypt')
        else:
            raise Exception('Check arguments passed !')
    except Exception as ex:
        print(f"RESET ADMIN EX : {ex}")
    else:
        return response
#-------------------------------
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
#-------------------------------
get_master = get_master_template_data
check_auth = get_admin_authenticate
set_auth = set_admin_authenticate
reset_auth = reset_admin_authenticate
#-----------------------------------------------------------------

def panel(request):

    if check_auth(request) == False:
        return redirect('panel_login')

    data = get_master()
    name = getCookie(request, 'admin_name')
    data['user_name'] = name[0].split()[0]

    return render(request, 'back/home.html', data)

def panel_login(request):

    if check_auth(request) == True:
        return redirect('panel')

    data = get_master()
    data['page'] = 'login'

    try:
        if request.method == 'POST':
            form_data = dict()
            temp = request.POST

            form_data['user'] = temp.get('user-id')
            form_data['pwd'] = temp.get('pwd')

            flag = False
            for val in form_data.values():
                if val == '' or val == None:
                    flag = True
                    break
            if flag == True:
                raise Exception('All Fields are Required !')
            else:
                flag = False
                user = set_auth(username=form_data['user'], password=form_data['pwd'])
                if user[0] == False:
                    raise Exception('Admin not found or Password incorrect !')
                else:
                    crypt = hashlib.md5(f"{form_data['user']}-{form_data['pwd']}".encode()).hexdigest()
                    del data['page']
                    data['user_name'] = user[1].split()[0]
                    return setCookie(request, file_path='back/home.html', data=data, crypt=crypt, admin_name=user[1])
    except Exception as ex:
        data['alert_type'] = 'ADMIN LOGIN ERROR'
        if 'NoneType' in str(ex):
            data['alert_message'] = 'Check The Credentials'
        else:
            data['alert_message'] = ex
        messages.info(request, data['alert_message'])

    return render(request, 'back/login.html', data)

def panel_logout(request):

    if check_auth(request) == False:
        return redirect('panel_login')
    
    data = get_master()
    data['site'] = 'login'
    return reset_auth(request, file_path='back/login.html', data=data)