from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^search/', views.search, name='search'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name='product_detail'),
    url(r'^occation/(?P<pk>\d+)/$', views.occation, name='occation'),

    url(r'^panel/occation/list/', views.occation_list, name='occation_list'),
    url(r'^panel/occation/add/', views.occation_add, name='occation_add'),
    url(r'^panel/occation/delete/(?P<pk>\d+)/$', views.occation_delete, name='occation_delete'),
    url(r'^panel/occation/edit/(?P<pk>\d+)/$', views.occation_edit, name='occation_edit'),

    url(r'^panel/product/list/', views.product_list, name='product_list'),
    url(r'^panel/product/add/', views.product_add, name='product_add'),
    url(r'^panel/product/delete/(?P<pk>\d+)/$', views.product_delete, name='product_delete'),
    url(r'^panel/product/edit/(?P<pk>\d+)/$', views.product_edit, name='product_edit'),
    
]