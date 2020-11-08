from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^api/add_user_bulk/(?P<word>.*)/$', views.add_user_bulk, name='api_add_user_bulk'),

]