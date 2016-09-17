from django.core.management import BaseCommand
import csv
from taplists.models import Bar
from taplists.models import Tap
from taplists.models import Style
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):

    help = "My tap import command"

    def handle(self, *args, **options):
        fields = ['brewery','beer','rating','beerurl','image','abv','ibu']
        for row in csv.reader(open('/home/BesTap/rating_builder/bestap_getter/OffPy'), delimiter='\t'):
            print "deleting %s from %s" % (row[6], row[0])
            rrow=[row[3],row[4],row[5],row[6],row[8],row[9],row[10]]
            t = Tap.objects.get(brewery=row[3], beer=row[4])
            b = Bar.objects.get(bar=row[0])
            t.bar.remove(b)

        for row in csv.reader(open('/home/BesTap/rating_builder/bestap_getter/NewPy'), delimiter='\t'):
            print row[6]
            try:
              s = Style.objects.get(style=row[7])
            except ObjectDoesNotExist:
                print '%s not in database' % row[7]
            rrow=[row[3],row[4],row[5],row[6],row[8],row[9],row[10]]
            t = Tap.objects.update_or_create(brewery=row[3], beer=row[4], defaults=dict(zip(fields, rrow)))
            b = Bar.objects.get(bar=row[0])
            t[0].bar.add(b)
            t[0].style.add(s)

        for row in csv.reader(open('/home/BesTap/rating_builder/bestap_getter/UpPy'), delimiter='\t'):
            print row[6]
            try:
              s = Style.objects.get(style=row[7])
            except ObjectDoesNotExist:
                print '%s not in database' % row[7]
            rrow=[row[3],row[4],row[5],row[6],row[8],row[9],row[10]]
            t = Tap.objects.update_or_create(brewery=row[3], beer=row[4], defaults=dict(zip(fields, rrow)))
            b = Bar.objects.get(bar=row[0])
            t[0].bar.add(b)
            t[0].style.add(s)
