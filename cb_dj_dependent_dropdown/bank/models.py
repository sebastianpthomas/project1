from django.db import models

# Create your models here.
class registration(models.Model):
    Name1 = models.CharField(max_length=250, unique=True)
    Password = models.CharField(max_length=250, unique=True)
    cpassword = models.CharField(max_length=250, unique=True)


class confir(models.Model):
    Name1 = models.CharField(max_length=250, unique=True)
    Password = models.CharField(max_length=250, unique=True)