from django.contrib import admin
from .models import Admins, Users, Images, Occations, Products

# Register your models here.

admin.site.register(Admins)
admin.site.register(Users)

admin.site.register(Products)

admin.site.register(Occations)
admin.site.register(Images)