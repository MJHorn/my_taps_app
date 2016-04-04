import django_filters
from .models import Tap

BARLIST=(
    ('tworow', 'Two Row'),
    ('thealehouseproject', 'Alehouse'),
)


class TapFilter(django_filters.FilterSet):
    bar = django_filters.MultipleChoiceFilter(choices=BARLIST)

    class Meta:
        model = Tap
        fields = ['bar']
