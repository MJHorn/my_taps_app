import django_filters
from .models import Tap
from .models import Bar
from django import forms

class TapFilter(django_filters.FilterSet):
    bar = django_filters.ModelMultipleChoiceFilter(queryset=Bar.objects.all(), label="", widget=forms.CheckboxSelectMultiple,help_text="")
    class Meta:
        model = Tap
        fields = ['bar']
