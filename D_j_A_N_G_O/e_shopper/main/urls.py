#-----CODE-----
from django.conf.urls import include
from django.urls import path
#from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_details/<pk>', views.product_details, name='product_details'),
    path('search/', views.search, name='search'),
]
#url(r'^about/$', views.about, name='about'),