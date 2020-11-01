from django.db import models
from django.db.models.deletion import CASCADE, ProtectedError, SET_NULL

from user.models import User
from product.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=SET_NULL)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.pk} | {self.user.name}'

