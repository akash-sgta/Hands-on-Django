"""gifthub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main.views import home_view as main_home
from main.views import about_view as main_about
from main.views import contact_view as main_contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_home, name='home'),
    path('home/', main_home, name='home'),
    path('contact/', main_contact, name='contact'),
    path('about/', main_about, name='about'),
]
