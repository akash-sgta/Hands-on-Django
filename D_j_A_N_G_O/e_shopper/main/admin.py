from django.contrib import admin

# Register your models here.
#-----CODE-----
from .models import Main
from .models import Slider
from .models import Occasion
from .models import Product

admin.site.register(Main)
admin.site.register(Slider)
admin.site.register(Occasion)
admin.site.register(Product)