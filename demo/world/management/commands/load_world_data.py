from functools import lru_cache

import requests
from django.core.management.base import BaseCommand

from world.models import Country, Continent


@lru_cache(maxsize=10)
def get_content(name):
    code = name.upper()[0:2]
    return Continent.objects.get_or_create(name=name, code=code)[0]


class Command(BaseCommand):
    help = 'Loads sample data from restcountries.eu'

    def handle(self, *args, **options):
        data = requests.get("https://restcountries.eu/rest/v2/all").json()

        for c in data:
            country, _ = Country.objects.update_or_create(code=c.get('alpha2Code'), defaults={
                'name': c.get('name'),
                'continent': get_content(c.get('region')),
                'area': c.get('area'),
                'population': c.get('population'),
            })

            country.city_set.update_or_create(name=c.get('capital'), defaults={
                'capital': True
            })

            print(".", end='')
