from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Style(models.Model):
    style = models.CharField(max_length=200)
    broadstyle = models.CharField(max_length=200, default='Shiraz')
    
    def __str__(self):
        return self.style

    class Meta:
        ordering = ('style',)

class Bar(models.Model):
    bar = models.CharField(max_length=200, default='FinshnPig')
    region = models.CharField(max_length=200, default='Farmville')
    state = models.CharField(max_length=200,default='NY')

    def __str__(self):
        return self.bar

    class Meta:
        ordering = ('bar','region')

class Tap(models.Model):
    bar = models.ManyToManyField(Bar,default='FinshnPig')
    brewery = models.CharField(max_length=200)
    beer = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=5, decimal_places=3)
    beerurl = models.CharField(max_length=200, default='https://untappd.com/b/the-alchemist-heady-topper/4691')
    style = models.ManyToManyField(Style)    
    image = models.CharField(max_length=200,default='http://vignette3.wikia.nocookie.net/pokemon/images/1/16/025Pikachu_OS_anime_10.png/revision/20150102074354')
    abv = models.DecimalField(max_digits=5, decimal_places=1,default=0)
    ibu = models.DecimalField(max_digits=5, decimal_places=1,default=0)

    def __str__(self):
        return self.beer
