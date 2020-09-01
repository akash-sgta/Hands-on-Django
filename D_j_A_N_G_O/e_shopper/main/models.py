#-----CODE-----
from __future__ import unicode_literals

from django.db import models

#-----CODE-----
class Main(models.Model):

    name = models.CharField(max_length=32)
    about = models.TextField(default='Default')
    summary = models.CharField(default="summary", max_length=32)

    facebook = models.CharField(max_length=128)
    twitter = models.CharField(max_length=128)
    instagram = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.pk}\t| {self.name}"

class Slider(models.Model):

    foreign_main_pk = models.CharField(default='0', max_length=4)
    foreign_ocassion_pk = models.CharField(default='0', max_length=4)

    catch_phrase = models.CharField(default="phrase", max_length=256)
    picture = models.ImageField(max_length=256, upload_to='home/slider')

    def __str__(self):

        site_name = Main.objects.get(pk=self.foreign_main_pk).name
        occasion = Occasion.objects.get(pk=self.foreign_ocassion_pk).name

        return f"{site_name}\t| {occasion}\t| {self.pk}"

class Occasion(models.Model):

    foreign_main_pk = models.CharField(default='1', max_length=4)

    name = models.CharField(max_length=32)

    def __str__(self):

        site_name = Main.objects.get(pk=self.foreign_main_pk).name

        return f"{site_name}\t| {self.name}\t| {self.pk}"

class Product(models.Model):

    foreign_main_pk = models.CharField(default='1', max_length=4)
    foreign_ocassion_pk = models.CharField(default='4', max_length=4)

    name = models.CharField(max_length=32)
    keyword = models.CharField(max_length=256)
    details = models.TextField(default="details")
    price = models.DecimalField(default='0.00', decimal_places=2, max_digits=10)
    brand = models.CharField(default='brand', max_length=256)
    picture = models.ImageField(max_length=256, upload_to='home/products')

    in_stock = models.DecimalField(default='1', decimal_places=0, max_digits=10)

    def __str__(self):

        site_name = Main.objects.get(pk=self.foreign_main_pk).name
        occasion = Occasion.objects.get(pk=self.foreign_ocassion_pk).name

        return f"{site_name}\t| {occasion}\t| {self.name}\t| {self.pk}"