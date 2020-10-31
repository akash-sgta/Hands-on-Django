from django.db import models
from django.http import request

# Create your models here.

class Main(models.Model):
    name = models.CharField(default='Site Name', max_length=127)
    summary = models.CharField(default='Site Summary', max_length=127)
    description = models.TextField(default='Site Description')
    address = models.CharField(default='Physical Office Address', max_length=225)

    def __str__(self):
        return f"{self.pk} | {self.name}"

class Cassarole(models.Model):
    quote = models.CharField(default='Quote', max_length=225)
    image_url = models.CharField(default='-', max_length=225)

    def __str__(self):
        return f"{self.pk} | {self.quote[:31]}"

class Developer(models.Model):
    name = models.CharField(default='Developer Name', max_length=127)
    email = models.EmailField()
    phone = models.CharField(default='+91-', max_length=15)
    designaiton = models.CharField(default='Developer Designation', max_length=127)
    
    image_name = models.CharField(default="-", max_length=127)
    image_url = models.CharField(default="-", max_length=127)

    def __str__(self):
        return f'{self.pk} | {self.name}'