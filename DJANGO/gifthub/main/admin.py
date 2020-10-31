from django.contrib import admin
# ======================================
from .models import Main,Cassarole,Developer

# Register your models here.

admin.site.register(Main)
admin.site.register(Cassarole)
admin.site.register(Developer)