from django.db import models

# Create your models here.

class Admin(models.Model):
    name = models.CharField(max_length=127, default='-')
    username = models.CharField(max_length=127, default='username')
    password = models.CharField(max_length=127, default='Passw0rd!')

    def __str__(self):
        return f'{self.pk} | {self.name}'