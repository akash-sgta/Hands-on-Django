from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^panel/user/list/', views.user_list, name='user_list'),
    # url(r'^panel/user/delete/(?P<pk>\d+)/$', views.user_list, name='user_list'),

    url(r'^user/login', views.user_login, name='user_login'),

]