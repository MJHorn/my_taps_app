import django_filters
from .models import Tap
from .models import Bar
from django import forms

BARLIST=(
    ('beerdeluxe', 'Beer Deluxe'),
    ('beerdeluxehawthorn', 'Beer Deluxe Hawthorn'),
    ('beermash', 'Beermash'),
    ('belgianbeercafemelbourne', 'Belgian Beer Cafe'),
    ('boatrockerbarrelroom', 'Boatrocker Barrel Room'),
    ('boilermakerhouse', 'Boilermaker House'),
    ('brotherburgerandthemarvellousbrew', 'Brother Burger'),
    ('brotherburgerandthemarvellousbrewsouthyarra', 'Brother Burger South Yarra'),
    ('carwyncellars', 'Carwyn Cellars'),
    ('eastofeverything', 'East of Everything'),
    ('forestershall', "Forester's Hall"),
    ('foxinthecorn', 'Fox in the Corn'),
    ('grapeandgrain', 'Grape and Grain'),
    ('littlehop', 'Little Hop'),
    ('moondogbrewery', 'Moon Dog Brewery'),
    ('sunmothcanteenbar', 'Sun Moth'),
    ('thealehouseproject', 'The Alehouse Project'),
    ('thecatfish', 'The Catfish'),
    ('thegertrudehotel', 'The Gertrude Hotel'),
    ('thelocaltaphousestk', 'The Local Taphouse'),
    ('theroyston', 'The Royston'),
    ('trubru', 'TRUBRU'),
    ('twobirdsbrewing', 'Two Birds Brewing'),
    ('upinsmoke', 'Up In Smoke'),
)

class TapFilter(django_filters.FilterSet):
    bar = django_filters.ModelMultipleChoiceFilter(label="", widget=forms.CheckboxSelectMultiple, choices=BARLIST,help_text="",)

    class Meta:
        model = Tap
        fields = ['bar']
