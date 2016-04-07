from django.core.management import BaseCommand
import csv
from taplists.models import Bar
from taplists.models import Tap
from taplists.models import Style

class Command(BaseCommand):

	help = "My tap import command"

	def handle(self, *args, **options):
		fields = ['brewery','beer','rating','beerurl']

		for row in csv.reader(open('/Users/transfer/Documents/Coding/BesTap/Some_Taps'), delimiter='\t'):
			print row
			b = Bar.objects.get(bar=row[0])
			s = Style.objects.get(style=row[5])
			rrow=[row[1],row[2],row[3],row[4]]
			t = Tap.objects.get_or_create(**dict(zip(fields, rrow)))
			t[0].bar.add(b)
			t[0].style.add(s)
