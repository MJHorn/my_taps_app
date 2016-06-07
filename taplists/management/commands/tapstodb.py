from django.core.management import BaseCommand
import csv
from taplists.models import Bar
from taplists.models import Tap
from taplists.models import Style

class Command(BaseCommand):

    help = "My tap import command"

    def handle(self, *args, **options):
        fields = ['brewery','beer','rating','beerurl','image','abv','ibu','state']

        for row in csv.reader(open('/home/BesTap/rating_builder/bestap_getter/Some_Taps'), delimiter='\t'):
            b = Bar.objects.get(bar=row[0])
            print row[6]
            s = Style.objects.get(style=row[7])
            rrow=[row[3],row[4],row[5],row[6],row[8],row[9],row[10],row[2]]
            t = Tap.objects.update_or_create(brewery=row[3], beer=row[4], state=row[2], defaults=dict(zip(fields, rrow)))
            t[0].bar.add(b)
            t[0].style.add(s)
