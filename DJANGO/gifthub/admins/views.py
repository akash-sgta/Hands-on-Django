from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from main.models import Main

# Create your views here.

def panel(request):

    if not request.user.is_authenticated:
        return redirect('panel_login')

    data = dict()
    data['page'] = 'home'
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

    data['user_name'] = request.user.username

    return render(request, 'back/home.html', data)

def panel_login(request):

    if request.user.is_authenticated:
        return redirect('panel')

    data = dict()
    data['page'] = 'login'
    
    scrub = Main.objects.get(pk=1)
    data['site_data'] = scrub

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
            data['alert_type'] = 'ERROR'
            data['alert_message'] = 'All Fields are Required !'
            return render(request, 'back/alert/login_like.html', data)
        else:

            flag = False
            user = authenticate(username=form_data['user'], password=form_data['pwd'])
            if user != None:
                login(request, user)
            else:
                flag = True

            if flag == True:
                data['alert_type'] = 'Email'
                data['alert_message'] = 'Admin not found or Password incorrect !'
                return render(request, 'back/alert/login_like.html', data)
            else:
                data['alert_type'] = 'Login Successful'
                html_src='''
                <a href='panel/home/' style='text-decoration:none;'>
                    <h3>Go To Panel</h3>
                </a>
                '''
                data['alert_message'] = html_src
                return render(request, 'back/alert/login_like.html', data)


    return render(request, 'back/login.html', data)

def panel_logout(request):
    logout(request)
    return redirect('panel_login')