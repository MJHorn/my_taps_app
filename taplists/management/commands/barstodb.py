from django.core.management import BaseCommand
import csv
from taplists.models import Bar

class Command(BaseCommand):

    help = "My bar import command"

    def handle(self, *args, **options):
        fields = ['bar','region']

        for row in csv.reader(open('/Users/transfer/Documents/Coding/BesTap/Bar_Names')):
            Bar.objects.create(**dict(zip(fields, row)))
