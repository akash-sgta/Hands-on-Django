from django.http import request
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage

from .models import Product, Occation
from main.models import Main, Cassarole
from admins.models import Admin
from user.models import User

import hashlib
# Create your views here.

# ------------------------------------------------------------------------------
def get_admin_authenticate(request):

    try:
        crypt = getCookie(request , 'crypt')
        if crypt[0] == 'NULL':
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
# ----------------------------
def get_master_template_data():
    data = dict()
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    return data
# ----------------------------
def get_home_template_data():
    data = get_master()

    scrub = Cassarole.objects.all()
    data['cassarole'] = scrub

    scrub = Occation.objects.all()
    data['occation'] = scrub

    scrub = Product.objects.all()
    data['product'] = scrub

    return data
# ----------------------------
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
# ----------------------------
def get_user_authenticate(request):

    try:
        crypt = getCookie(request , 'ucrypt')
        if crypt[0] == None:
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

# ----------------------------
check_admin_auth = get_admin_authenticate
get_master = get_master_template_data
get_home = get_home_template_data
check_user_auth = get_user_authenticate
# ------------------------------------------------------------------------------

def detail(request, pk):
    data = get_home()

    if check_user_auth(request) == True:
        data['is_auth'] = True
        data['user_name'] = getCookie(request, 'user_name')[0].split()[0]

    try:
        scrub = Product.objects.get(pk=pk)
        data['pr'] = scrub
    except:
        data['alert_type'] = 'Product Not Found ERROR'
        data['alert_message'] = 'Item does not exist, check picker<br>Rollback !'
        return render(request, 'front/alert/home_like.html', data)


    return render(request, 'front/product/detail.html', data)

def occation_list(request):

    if check_admin_auth(request) == False:
        return redirect('panel_login')

    data = dict()
    data['page'] = 'occations'

    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    scrub = Occation.objects.all().order_by('-pk')
    data['occation_detail'] = scrub

    return render(request, 'back/occation/show_occations.html', data)

def occation_add(request):

    if check_admin_auth(request) == False:
        return redirect('panel_login')

    data = dict()

    scrap = Main.objects.get(pk=1)
    data['site_data'] = scrap

    if request.method == 'POST':
        form_data = dict()
        temp = request.POST
        print(temp)

        form_data['occation'] = temp.get('prod-occation')
        
        flag = False
        for val in form_data.values():
            if val == '' or val == None:
                flag = True
                break
        
        if flag == True:
            data['alert_type'] = 'Occation Add ERROR'
            data['alert_message'] = 'All Fields are Required !'
            return render(request, 'back/alert/base_like.html', data)
        else:
            oc = Occation.objects.all()
            flag = False
            for i in oc:
                if ((str(i.name).lower() in str(form_data['occation']).lower()) or
                    str(form_data['occation']).lower() in (str(i.name).lower())):
                    flag = True
                    break
            
            if flag:
                data['alert_type'] = 'Occation Add ERROR'
                data['alert_message'] = 'Occation already exists !'
                return render(request, 'back/alert/base_like.html', data)
            else:
                try:
                    form = Occation(name = form_data['occation'])
                    form.save()
                except Exception as e:
                    data['alert_type'] = 'Occation Add ERROR'
                    data['alert_message'] = e
                    return render(request, 'back/alert/base_like.html', data)
                else:
                    return redirect('occation_list')

    return render(request, 'back/occation/occation_add.html', data)

def occation_delete(request, pk):

    if check_admin_auth(request) == False:
        return redirect('panel_login')
    
    data = dict()
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    try:
        form = Occation.objects.get(pk=int(pk))
    except Exception as e:
        data['alert_type'] = 'Occation Delete ERROR'
        data['alert_message'] = "Occation does not exist, check picker<br><a href='#'>Rollback !</a>"
        return render(request, 'back/alert/base_like.html', data)
    else:
        form.delete()
        return redirect('occation_list')

def occation_edit(request, pk):

    if check_admin_auth(request) == False:
        return redirect('panel_login')
    
    data = dict()
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    if request.method == 'POST':
        temp = request.POST
        form_data = dict()

        try:
            form = Occation.objects.get(pk=pk)
        except Exception as ex:
            data['alert_type'] = 'Occation Edit ERROR'
            data['alert_message'] = "Occation does not exist, check picker<br><a href='#'>Rollback !</a>"
            return render(request, 'back/alert/base_like.html', data)
        else:
            form_data['name'] = temp.get('prod-occation')
            
            flag = False
            for i in Occation.objects.all():
                if((str(i.name).lower() in str(form_data['name']).lower()) or
                (str(form_data['name']).lower() in str(i.name)).lower()):
                    flag = True
                    break
            
            if flag == True:
                data['alert_type'] = 'Occation Edit ERROR'
                data['alert_message'] = "Occation already exists !"
                return render(request, 'back/alert/base_like.html', data)
            else:
                form = Occation.objects.get(pk=pk)
                form.name = form_data['name']
                form.save()
                return redirect('occation_list')
    else:
        try:
            data['old_content'] = Occation.objects.get(pk=pk)
        except Exception as ex:
            data['alert_type'] = 'Occation Edit ERROR'
            data['alert_message'] = "Occation does not exist, check picker<br><a href='#'>Rollback !</a>"
            return render(request, 'back/alert/base_like.html', data)
        else:
            return render(request, 'back/occation/occation_edit.html', data)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def product_list(request):

    if check_admin_auth(request) == False:
        return redirect('panel_login')

    data = dict()
    data['page'] = 'products'
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    scrub = Product.objects.all().order_by('stock').order_by('-pk')
    data['product_detail'] = scrub

    return render(request, 'back/product/show_products.html', data)

def product_add(request):

    if check_admin_auth(request) == False:
        return redirect('panel_login')

    data = dict()

    scrap = Main.objects.get(pk=1)
    data['site_data'] = scrap

    if request.method == 'POST':
        form_data = dict()
        temp = request.POST

        form_data['name'] = temp.get('prod-name')
        form_data['details'] = temp.get('prod-details')
        form_data['price'] = temp.get('prod-price')
        form_data['brand'] = temp.get('prod-brand')
        form_data['stock'] = temp.get('prod-stock')
        form_data['occation'] = temp.get('prod-occation')
        
        flag = False
        for key,val in form_data.items():
            if val == '' or val == None:
                flag = True
                break
        
        if flag == True:
            data['alert_type'] = 'Product Add ERROR'
            data['alert_message'] = 'All Fields are Required !'
            return render(request, 'back/alert/base_like.html', data)
        else:
            form_data['occation'] = Occation.objects.get(pk = int(form_data['occation']))

        try:
            image_file = request.FILES['prod-image']
        
            if str(image_file.content_type).startswith("image"):
                if image_file.size < 5000000:
                    fs = FileSystemStorage()
                    file_name = fs.save(image_file.name, image_file)
                    url = fs.url(file_name)
                else:
                    raise Exception("Image size more than 5mb !")
            else:
                raise Exception("Image Required !")
        except Exception as e:
            data['alert-type'] = 'Product Add ERROR'
            data['alert-message'] = e
            return render(request, 'back/alert/base_like.html', data)
        else:
            form_data['image_url'] = url
            form_data['image_name'] = file_name
            try:
                form = Product(name = form_data['name'],
                            details = form_data['details'],
                            price = form_data['price'],
                            brand = form_data['brand'],
                            stock = form_data['stock'],
                            occation = form_data['occation'],
                            image_url = form_data['image_url'],
                            image_name = form_data['image_name'])
                form.save()
            except Exception as e:
                data['alert_type'] = 'Product Add ERROR'
                data['alert_message'] = e
                return render(request, 'back/alert/base_like.html', data)
            else:
                return redirect('product_list')

    data['occation_list'] = Occation.objects.all()

    return render(request, 'back/product/product_add.html', data)

def product_delete(request, pk):

    if check_admin_auth(request) == False:
        return redirect('panel_login')
    
    data = dict()
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    try:
        form = Product.objects.get(pk=int(pk))
    except Exception as e:
        data['alert_type'] = 'Product Delete ERROR'
        data['alert_message'] = "Product does not exist, check picker<br><a href='#'>Rollback !</a>"
        return render(request, 'back/alert/base_like.html', data)
    else:
        form.delete()
        return redirect('product_list')

def product_edit(request, pk):

    if check_admin_auth(request) == False:
        return redirect('panel_login')
    
    data = dict()
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    if request.method == 'POST':
        temp = request.POST
        form_data = dict()

        try:
            form = Product.objects.get(pk=pk)
        except Exception as ex:
            data['alert_type'] = 'Product Edit ERROR'
            data['alert_message'] = "Product does not exist, check picker<br><a href='#'>Rollback !</a>"
            return render(request, 'back/alert/base_like.html', data)
        else:
            form_data['name'] = temp.get('prod-name')
            form_data['details'] = temp.get('prod-details')
            form_data['price'] = temp.get('prod-price')
            form_data['brand'] = temp.get('prod-brand')
            form_data['stock'] = temp.get('prod-stock')
            form_data['occation'] = temp.get('prod-occation')
            
            flag = False
            for val in form_data.values():
                if val == '' or val == None:
                    flag = True
                    break
        
            if flag == True:
                data['alert_type'] = 'Product Edit ERROR'
                data['alert_message'] = 'All Fields are Required !'
                return render(request, 'back/alert/base_like.html', data)
            
            flag = False
            for i in Occation.objects.all():
                if( int(i.pk) == int(form_data['occation']) ):
                    flag = True
                    break
            
            if flag == False:
                data['alert_type'] = 'Product Edit ERROR'
                data['alert_message'] = "Occation does not exist !"
                return render(request, 'back/alert/base_like.html', data)
            else:
                try:
                    try:
                        image_file = request.FILES['prod-image']
                    except Exception as e:
                            print(f"EX : {e}")
                            flag = False
                    else:
                        flag =True
                    
                    form = Product.objects.get(pk=pk)

                    if flag:
                        if str(image_file.content_type).startswith("image"):
                            if image_file.size < 5000000:
                            
                                fs = FileSystemStorage()
                                file_name = fs.save(image_file.name, image_file)
                                url = fs.url(file_name)        
                            
                                fss = FileSystemStorage()
                                fss.delete(form.image_name)

                                form.image_name = file_name
                                form.image_url = url
                        
                            else:
                                raise Exception("Image File Should be less than 5MB")
                    else:
                        pass

                    form.name = form_data['name']
                    form.details = form_data['details']
                    form.price = form_data['price']
                    form.stock = form_data['stock']
                    form.occation = Occation.objects.get(pk = int(form_data['occation']))
                    form.name = form_data['name']
                    form.save()

                except Exception as e:
                    print(f"Ex : {e}")
                    data['alert_type'] = 'Product Edit ERROR'
                    if 'prod-image' in str(e):
                        data['alert_message'] = 'Image Required !'
                    else:
                        data['alert_message'] = e
                    return render(request, 'back/alert/base_like.html', data)
                else:
                    return redirect('product_list')
    else:
        try:
            data['old_content'] = Product.objects.get(pk=pk)
        except Exception as ex:
            data['alert_type'] = 'Product Edit ERROR'
            data['alert_message'] = "Product does not exist, check picker<br><a href='#'>Rollback !</a>"
            return render(request, 'back/alert/base_like.html', data)
        else:
            scrub = Occation.objects.all()
            data['occation_list'] = scrub
            return render(request, 'back/product/product_edit.html', data)
