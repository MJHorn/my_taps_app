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

class TapFilter(django_filters.FilterSet):
    bar__region = django_filters.MultipleChoiceFilter(choices=CHOICES, label="Regions:", widget=forms.CheckboxSelectMultiple,help_text="")
    style__broadstyle = django_filters.MultipleChoiceFilter(choices=STYLES, label="Styles:", widget=forms.CheckboxSelectMultiple,help_text="")

class StyleFilter(django_filters.FilterSet):
    style = django_filters.ModelMultipleChoiceFilter(queryset=Style.objects.all(), label="", widget=forms.CheckboxSelectMultiple,help_text="")
    class Meta:
        model = Tap
        fields = ['style']
