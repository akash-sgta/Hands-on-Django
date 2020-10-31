from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(default="Full Name", max_length=255)
    email = models.EmailField()
    password = models.CharField(default="Passw0rd!", max_length=31)
    address = models.TextField(default="Address Full")
    phone = models.CharField(default="+91-", max_length=15)

    def __str__(self):
        return f"{self.pk} | {self.name.split()[0]}"