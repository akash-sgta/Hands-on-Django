# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.deletion import SET_DEFAULT


class Admins(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    token = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'admins'
    
    def __str__(self):
        return f"{self.pk} | {self.f_name}"


class Images(models.Model):
    src = models.ImageField(upload_to='uploads/%Y/%m/%d')
    name = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'images'
    
    def __str__(self):
        return f"{self.pk} | {self.name}"


class Occations(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'occations'
    
    def __str__(self):
        return f"{self.pk} | {self.name}"


class Products(models.Model):
    name = models.CharField(max_length=255)
    keyword_1 = models.CharField(max_length=32)
    keyword_2 = models.CharField(max_length=32, blank=True, null=True)
    details = models.CharField(max_length=2047)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    occation = models.ForeignKey(Occations, on_delete=models.SET_DEFAULT, default=1)
    brand = models.CharField(max_length=255)
    image = models.ForeignKey(Images, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        managed = True
        db_table = 'products'
    
    def __str__(self):
        return f"{self.pk} | {self.name}"


class Users(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    pass_field = models.CharField(db_column='pass', max_length=255)  # Field renamed because it was a Python reserved word.
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    state_in = models.CharField(max_length=63)
    district = models.CharField(max_length=127)
    pincode = models.IntegerField()
    phone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'
    
    def __str__(self):
        return f"{self.pk} | {self.f_name}"
