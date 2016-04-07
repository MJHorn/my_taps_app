from django.db import models

class Style(models.Model):
    style = models.CharField(max_length=200)
    
    def __str__(self):
        return self.style

    class Meta:
        ordering = ('style',)

class Bar(models.Model):
    bar = models.CharField(max_length=200)

    def __str__(self):
        return self.bar

    class Meta:
        ordering = ('bar',)

class Tap(models.Model):
    bar = models.ManyToManyField(Bar)
    brewery = models.CharField(max_length=200)
    beer = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=5, decimal_places=3)
    beerurl = models.CharField(max_length=200, default='https://untappd.com/b/the-alchemist-heady-topper/4691')
    style = models.ManyToManyField(Style)    

    def __str__(self):
        return self.beer
