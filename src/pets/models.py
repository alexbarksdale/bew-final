from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    pet_name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    weight_in_pounds = models.DecimalField(max_digits=5, decimal_places=2)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
