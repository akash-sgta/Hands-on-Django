from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^admin/', views.panel_login, name='panel_login'),
    url(r'^panel/login/', views.panel_login, name='panel_login'),
    url(r'^panel/home/', views.panel, name='panel'),
    url(r'^panel/logout/', views.panel_logout, name='panel_logout'),

]