from os import name
from django.http import request, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.middleware import csrf

from product.models import Product,Occation
from product.views import Tag_Generator_Util

import json
import pandas
import base64
import hashlib
import datetime
# Create your views here.

def put_products(data):

    try:
        message = ''
        product_ref = Product(name = data['Name'],
                              details = data['Details'],
                              price = data['Price'],
                              brand = data['Brand'],
                              stock = data['Stock'])
        product_ref.save()

        occation_refs = Occation.objects.filter(pk = int(data['Occation']))
        if len(occation_refs) == 0:
            message += f", {data['Name']}-Mannually add occation"
        else:
            product_ref.occation = occation_refs[0]
            product_ref.save()
        
        try:
            stamp = datetime.datetime.now()
            img_bt = (data['Image'][2:-1]).encode().decode('unicode-escape').encode('ISO-8859-1')
            
            img_name = "{}:{}_{}_{}:{}_{}_{}.jpg".format(data['Name'], stamp.day, stamp.month, stamp.year, stamp.hour, stamp.minute, stamp.second)
            img_url = 'media/{}'.format(img_name)
            with open(img_url, 'wb') as target:
                target.write(img_bt)
            
            product_ref.image_name = img_name
            product_ref.image_url = f"/{img_url}"
            product_ref.save()
        except:
            message += f", {data['Name']}-Mannually add Image"
        
        prod_pk = Product.objects.latest('pk').pk
        tgu_ref = Tag_Generator_Util(prod_pk, data['Tag_String'])
        tgu_ref.start()
        tgu_ref.join()
        
    except Exception as ex:
        return False, f"EX : {ex}"
    else:
        return True, message

def add_user_bulk(request, word):

    try:
        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'show_example':
                print('Show Example')
            if action == 'enrty_data':
                print('DATA ENTRY')
                data = request.POST.get('data')
                hash = request.POST.get('hash')
                check_hash = hashlib.md5(data.encode()).digest()
                check_hash = str(check_hash)[2:-1]
                if check_hash == hash:
                    print("CHECK PASS")
                    form_data = base64.b64decode(data).decode()
                    form_data = json.loads(form_data)
                    for row in form_data.values():
                        print(put_products(row))

                    return JsonResponse(data={"ACTION":"True"}, safe=True)
                else:
                    return JsonResponse(data={"ACTION":"False"}, safe=True)
        else:
            data = dict()
            if word == 'initiate':
                data['TOKEN'] = str(csrf.get_token(request))
                data['OcLim'] = {"high" : Occation.objects.all().order_by('-pk')[0].pk, "low" : Occation.objects.all().order_by('pk')[0].pk}
            else:
                data['ERROR'] = 'ONLY -POST- ACCEPTED, for client-end support contact developers ! '
            
            return JsonResponse(data, safe=True)
    except Exception as ex:
        print(f"API ERROR : {ex}")
        return JsonResponse(data={"ACTION":"False"}, safe=True)

