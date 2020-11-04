from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^panel/user/list/', views.user_list, name='user_list'),
    # url(r'^panel/user/delete/(?P<pk>\d+)/$', views.user_list, name='user_list'),

    url(r'^user/login', views.user_login, name='user_login'),
    url(r'^user/logout', views.user_logout, name='user_logout'),

    url(r'^order/put', views.put_order, name='put_order'),
    url(r'^order/show', views.show_order, name='show_order'),
    url(r'^order/confirm', views.confirm_order, name='confirm_order'),

    url(r'^order/reset/ugabuganiganiga/', views.reset_orders, name='reset_orders'),

]