import django_filters
from .models import Tap
from .models import Bar
from .models import Style
from django import forms
from django.db.models import Q

CHOICES = (
    ('CBD', 'CBD'),
    ('Inner North', 'Inner North'),
    ('North', 'North'),
    ('South', 'South'),
    ('East', 'East'),
    ('West', 'West'),
)

class TapFilter(django_filters.FilterSet):
    bar__region = django_filters.MultipleChoiceFilter(choices=CHOICES, label="Regions:", widget=forms.CheckboxSelectMultiple,help_text="")
    bar = django_filters.ModelMultipleChoiceFilter(queryset=Bar.objects.all(), label="Bars:", widget=forms.CheckboxSelectMultiple,help_text="")


class StyleFilter(django_filters.FilterSet):
    style = django_filters.ModelMultipleChoiceFilter(queryset=Style.objects.all(), label="", widget=forms.CheckboxSelectMultiple,help_text="")
    class Meta:
        model = Tap
        fields = ['style']

