from django.core.management import BaseCommand
import csv
from taplists.models import Style
import codecs

class Command(BaseCommand):

    help = "My style import command"

    def handle(self, *args, **options):
        fields = ['style','broadstyle']

        for row in csv.reader(codecs.open('/Users/transfer/Documents/Coding/BesTap/Style_Guide'), delimiter=','):
            Style.objects.create(**dict(zip(fields, row)))
