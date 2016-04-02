from django.db import models
from django.utils import timezone


class Tap(models.Model):
    bar = models.CharField(max_length=200)
    brewery = models.CharField(max_length=200)
    beer = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.beer
