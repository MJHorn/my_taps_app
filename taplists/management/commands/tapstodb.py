from django.core.management import BaseCommand
import csv
from taplists.models import Tap

class Command(BaseCommand):

	help = "My tap import command"

	def handle(self, *args, **options):
		fields = ['bar','brewery','beer','rating']

		for row in csv.reader(open('/Users/transfer/Documents/Coding/BesTap/Some_Taps'), delimiter='\t'):
			Tap.objects.create(**dict(zip(fields, row)))
