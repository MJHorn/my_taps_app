from django.core.management import BaseCommand
import csv
from taplists.models import Bar

class Command(BaseCommand):

    help = "My bar import command"

    def handle(self, *args, **options):
        fields = ['bar','region','state']

        for row in csv.reader(open('/home/BesTap/rating_builder/bestap_getter/Bar_Names')):
            Bar.objects.create(**dict(zip(fields, row)))
