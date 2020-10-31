from django.contrib import admin
# ==============================
from .models import Occation, Product

# Register your models here.

admin.site.register(Occation)
admin.site.register(Product)