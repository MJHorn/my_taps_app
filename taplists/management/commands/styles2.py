from django.core.management import BaseCommand
import csv
from taplists.models import Style
import codecs

class Command(BaseCommand):

    help = "My style import command"

    def handle(self, *args, **options):
        fields = ['style','broadstyle']

        Style.objects.all().delete()

        for row in csv.reader(codecs.open('/home/BesTap/rating_builder/bestap_getter/Style_Guide'), delimiter=','):
            Style.objects.get_or_create(**dict(zip(fields, row)))
