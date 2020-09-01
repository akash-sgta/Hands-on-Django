from django.shortcuts import render
#-----CODE-----
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Main
from .models import Slider
from .models import Occasion
from .models import Product

site_picker = 1

def scrape_from_main(pk):
    pull_from_main = Main.objects.get(pk=site_picker)

    mid = len(pull_from_main.name)//2
    site_name_f = pull_from_main.name[:mid+1]
    site_name_l = pull_from_main.name[mid+1:]
    site_summary = pull_from_main.summary

    return site_name_f, site_name_l, site_summary

def home(request):

    site_name_f, site_name_l, site_summary = scrape_from_main(site_picker)

    pull_from_slider = Slider.objects.filter(foreign_main_pk=site_picker)

    slider_0 = pull_from_slider[0]
    slider_rest = pull_from_slider[1:]

    pull_from_ocassion = Occasion.objects.all()

    pull_from_product = Product.objects.filter(foreign_main_pk=site_picker)
    pull_tags = Product.objects.filter(foreign_main_pk=site_picker).values_list('keyword', flat=True).distinct()

    
    push_to_home = {
            'site_name_f' : site_name_f,
            'site_name_l' : site_name_l,
            'site_summary' : site_summary,
            'slider_0' : slider_0,
            'slider_rest' : slider_rest,
            'catagories' : pull_from_ocassion,
            'products' : pull_from_product,
            'tags' : pull_tags,
    }


    return render(request, 'front/home.html', push_to_home)

def product_details(request, pk):

    site_name_f, site_name_l, site_summary = scrape_from_main(site_picker)

    pull_from_ocassion = Occasion.objects.all()

    pull_from_product = Product.objects.get(pk=pk)

    push_to_product_details = {
        'site_name_f' : site_name_f,
        'site_name_l' : site_name_l,
        'site_summary' : site_summary,
        'catagories' : pull_from_ocassion,
        'product' : pull_from_product,
    }
    
    return render(request, 'front/product_details.html', push_to_product_details)

def search(request):

    query = str(request.GET['query'])
    print("Q U E R Y : ",query)

    site_name_f, site_name_l, site_summary = scrape_from_main(site_picker)

    pull_from_slider = Slider.objects.filter(foreign_main_pk=site_picker)

    slider_0 = pull_from_slider[0]
    slider_rest = pull_from_slider[1:]

    pull_from_ocassion = Occasion.objects.all()

    pull_from_product = Product.objects.filter(foreign_main_pk=site_picker).filter(keyword=query)

    pull_tags = Product.objects.filter(foreign_main_pk=site_picker).values_list('keyword', flat=True).distinct()

    push_to_home = {
        'site_name_f' : site_name_f,
        'site_name_l' : site_name_l,
        'site_summary' : site_summary,
        'slider_0' : slider_0,
        'slider_rest' : slider_rest,
        'catagories' : pull_from_ocassion,
        'products' : pull_from_product,
        'tags' : pull_tags,
    }
    
    return render(request, 'front/home.html', push_to_home)
