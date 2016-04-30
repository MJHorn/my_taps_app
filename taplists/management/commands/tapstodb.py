from django.core.management import BaseCommand
import csv
from taplists.models import Bar
from taplists.models import Tap
from taplists.models import Style

class Command(BaseCommand):

    help = "My tap import command"

    def handle(self, *args, **options):
        fields = ['brewery','beer','rating','beerurl','image']

        for row in csv.reader(open('/home/BesTap/rating_builder/bestap_getter/Some_Taps'), delimiter='\t'):
            b = Bar.objects.get(bar=row[0])
            s = Style.objects.get(style=row[6])
            rrow=[row[2],row[3],row[4],row[5],row[7]]
            t = Tap.objects.update_or_create(brewery=row[2], beer=row[3], defaults=dict(zip(fields, rrow)))
            t[0].bar.add(b)
            t[0].style.add(s)
