from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
# ====================================

# Create your models here.

class Occation(models.Model):
    name = models.CharField(default="Occation", max_length=63)

    def __str__(self):
        return f"{self.pk} | {self.name}"

class Product(models.Model):
    name = models.CharField(default="Product Name", max_length=127)
    details = models.TextField(default="Product Details")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    brand = models.CharField(default="Brand Name", max_length=127)
    stock = models.IntegerField(default=1)

    occation = models.ForeignKey(Occation, null=True, blank=True, on_delete=SET_NULL)
    
    image_name = models.CharField(default="-", max_length=127)
    image_url = models.CharField(default="-", max_length=127)

    def __str__(self):
        return f"{self.pk} | {self.name}"
