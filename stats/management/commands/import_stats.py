import csv

from django.core.management.base import BaseCommand
from stats.models import TempStat

class Command(BaseCommand):
    help = 'Import data'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--csv', required=True)

    def handle(self, *args, **options):
        file = options["csv"]

        with open(file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                year=row["year"]
                if not year:
                    continue

                annual_mean = row["annual_mean"]
                if not annual_mean:
                    annual_mean = 'NaN'

                moving_mean = row["moving_mean"]
                if not moving_mean:
                    moving_mean = 'NaN'
                
                stat, created = TempStat.objects.get_or_create(
                    year= year,
                    annual_mean=annual_mean,
                    moving_mean=moving_mean,
                )