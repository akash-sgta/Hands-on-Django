from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^cart/show', views.show_cart, name='show_cart'),
    url(r'^cart/add', views.add_to_cart, name='add_to_cart'),

]