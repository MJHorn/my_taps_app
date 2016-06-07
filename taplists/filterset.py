import django_filters
from .models import Tap
from .models import Bar
from .models import Style
from django import forms

CHOICES = (
    ('CBD', 'CBD'),
    ('Inner North', 'Inner North'),
    ('North', 'North'),
    ('South', 'South'),
    ('East', 'East'),
    ('West', 'West'),
    ('Regional VIC', 'Regional VIC'),
)

STYLES = (
    ('Pale / Golden','Pale / Golden'),
    ('IPA / Amber','IPA / Amber'),
    ('Lager','Lager'),
    ('Saison / Wheat','Saison / Wheat'),
    ('Sour','Sour'),
    ('Brown / Porter / Stout','Brown / Porter / Stout'),
    ('Strong Ale / Barleywine','Strong Ale / Barleywine'),
    ('Cider','Cider'),
    ('Other','Other'),
)

class TapFilterMin(django_filters.FilterSet):
    style__broadstyle = django_filters.MultipleChoiceFilter(choices=STYLES, label="Styles:", widget=forms.CheckboxSelectMultiple(attrs={'class' : 'myfieldclass'}),help_text="")
    class Meta:
        order_by = [('-rating','Rating'),('-abv','ABV'),('-ibu','IBU')]

class TapFilter(django_filters.FilterSet):
    bar__region = django_filters.MultipleChoiceFilter(choices=CHOICES, label="Regions:", widget=forms.CheckboxSelectMultiple(attrs={'class' : 'myfieldclass'}),help_text="")
    style__broadstyle = django_filters.MultipleChoiceFilter(choices=STYLES, label="Styles:", widget=forms.CheckboxSelectMultiple(attrs={'class' : 'myfieldclass'}),help_text="")
    class Meta:
        order_by = [('-rating','Rating'),('-abv','ABV'),('-ibu','IBU')]

class MTapFilterMin(django_filters.FilterSet):
    style__broadstyle = django_filters.MultipleChoiceFilter(choices=STYLES, label="Filter Styles:", widget=forms.SelectMultiple(attrs={'class' : 'styleclass','onchange' : 'this.form.submit()'}),help_text="")

class MTapFilter(django_filters.FilterSet):
    bar__region = django_filters.MultipleChoiceFilter(choices=CHOICES, label="Filter Regions:", widget=forms.SelectMultiple(attrs={'class' : 'barclass','onchange' : 'this.form.submit()'}),help_text="")
    style__broadstyle = django_filters.MultipleChoiceFilter(choices=STYLES, label="Filter Styles:", widget=forms.SelectMultiple(attrs={'class' : 'styleclass','onchange' : 'this.form.submit()'}),help_text="")

class StyleFilter(django_filters.FilterSet):
    style = django_filters.ModelMultipleChoiceFilter(queryset=Style.objects.all(), label="", widget=forms.CheckboxSelectMultiple,help_text="")
    class Meta:
        model = Tap
        fields = ['style']
