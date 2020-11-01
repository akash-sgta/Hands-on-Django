from django.http import request
from django.shortcuts import redirect, render


from .models import User
from main.models import Main

import time
# Create your views here.

def user_list(request):

    if not request.user.is_authenticated:
        return redirect('panel_login')

    data = dict()
    data['page'] = 'users'
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    scrub = User.objects.all().order_by('-pk')
    data['user_detail'] = scrub

    return render(request, 'back/user/show_users.html', data)

def user_login(request):

    data = dict()

    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

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
                        break
                if flag == 0:
                    data['alert_type'] = 'LOGIN ERROR'
                    raise Exception("Email not registered !")
                elif flag == 1:
                    data['alert_type'] = 'LOGIN ERROR'
                    raise Exception("Password Incorrect !")
                else:
                    return redirect('home')

        
        except Exception as e:
            data['alert_message'] = e
            return render(request, 'front/alert/home_like.html', data)
            

    return render(request, 'front/user/login.html', data)