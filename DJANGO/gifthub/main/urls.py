from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^developer/', views.developer, name='developer'),

    url(r'^404', views.get_404, name='get_404'),
]