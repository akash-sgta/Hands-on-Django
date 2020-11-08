from django.contrib import admin
# ==============================
from .models import Occation, Product, Tag

# Register your models here.

admin.site.register(Occation)
admin.site.register(Product)
admin.site.register(Tag)