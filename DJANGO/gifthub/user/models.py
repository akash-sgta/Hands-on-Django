from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

from product.models import Product
# Create your models here.

class User(models.Model):
    name = models.CharField(default="Full Name", max_length=255)
    email = models.EmailField()
    password = models.CharField(default="Passw0rd!", max_length=31)
    address = models.TextField(default="Address Full")
    phone = models.CharField(default="+91-", max_length=15)

    def __str__(self):
        return f"{self.pk} | {self.name.split()[0]}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True, blank=True)
    address = models.TextField(default='-')
    phone = models.CharField(max_length=20, default='0')
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} | {self.user.name} | {self.product.name} | {self.completed}"