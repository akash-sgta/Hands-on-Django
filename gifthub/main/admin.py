from django.contrib import admin
from .models import District, State, User, Admin, Image, Occation, Product
# Register your models here.

admin.site.register(District)
admin.site.register(State)
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Image)
admin.site.register(Occation)
admin.site.register(Product)

# admin.site.register()