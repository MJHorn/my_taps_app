from django.core.management import BaseCommand
import csv
from taplists.models import Bar

class Command(BaseCommand):

    help = "My bar import command"

    def handle(self, *args, **options):
        fields = ['bar','region','state']

        for row in csv.reader(open('/home/BesTap/rating_builder/bestap_getter/Bars_Names_Regions')):
            info = row[1:4]
            Bar.objects.update_or_create(bar=row[1], defaults=dict(zip(fields, info)))
