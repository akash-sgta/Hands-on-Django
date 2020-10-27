from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
import random

from django.db.models.fields import NullBooleanField
# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=63, default='Default District')

    def __str__(self):
        return f'{self.pk} | {self.name}'

class State(models.Model):
    name = models.CharField(max_length=63, default='Default State')
    capital = models.ForeignKey(District, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.capital == None:
            return f'{self.pk} | {self.name} || NONE'
        else:
            return f'{self.pk} | {self.name} || {self.capital.name}'

class User(models.Model):
    f_name = models.CharField(max_length=127, default='First Name')
    l_name = models.CharField(max_length=127, default='Last Name', blank=True, null=True)
    email = models.EmailField(default='mailid@domain.com')
    password = models.CharField(max_length=31, default='Passw0rd!')
    address = models.TextField(default='Address')
    state = models.ForeignKey(State, null=True, blank=True, on_delete=SET_NULL)
    district = models.ForeignKey(District, null=True, blank=True, on_delete=SET_NULL)
    pincode = models.IntegerField(default=700001)
    phone = models.CharField(max_length=20, default='+91 9999999999')

    def __str__(self):
        return f'{self.pk} | {self.f_name} | {self.l_name}'

class Admin(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE)
    password = models.CharField(max_length=31, default='Passw0rd!!!!!')
    token = models.CharField(max_length=255, default='xxgenerateTokenxx')

    def __str__(self):
        return f'{self.pk} || {self.user.f_name}'

class Image(models.Model):
    name = models.CharField(max_length=31)
    src_1 = models.ImageField(upload_to='upload/%Y/%m/%d')
    src_2 = models.ImageField(upload_to='upload/%Y/%m/%d')
    src_3 = models.ImageField(upload_to='upload/%Y/%m/%d')

    def __str__(self):
        return f'{self.pk} | {self.name}'

class Occation(models.Model):
    name = models.CharField(max_length=255, default='Occation')

    def __str__(self):
        return f'{self.pk} | {self.name}'

class Product(models.Model):
    name = models.CharField(max_length=127, default='Product Name')
    keyword_1 = models.CharField(max_length=31, default='keyword')
    keyword_2 = models.CharField(max_length=31, null=True, blank=True)
    details = models.TextField(default='Product Details')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    brand = models.CharField(max_length=127, default='Brand')
    occation = models.ForeignKey(Occation, null=True, blank=True, on_delete=SET_NULL)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=SET_NULL)
    features = models.BooleanField(default=False)

    def __str__(self):
        occ = self.occation
        if occ == None:
            occ = 'NONE'
        else:
            occ = occ.name
        return f'{self.pk} | {self.name} || {occ}'
