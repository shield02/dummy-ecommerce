from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.EmailField(max_length=254)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=32)

