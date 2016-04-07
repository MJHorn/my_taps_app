from django.core.management import BaseCommand
import csv
from taplists.models import Style

class Command(BaseCommand):

	help = "My style import command"

	def handle(self, *args, **options):
		fields = ['style']

		for row in csv.reader(open('/Users/transfer/Documents/Coding/BesTap/Style_Names'), delimiter='\t'):
			Style.objects.create(**dict(zip(fields, row)))
