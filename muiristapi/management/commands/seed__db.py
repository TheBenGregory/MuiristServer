"""
seed the db:
python3 manage.py seed_db
(file name)
    """

from django.core.management.base import BaseCommand
import requests
from muiristapi.models import Park


class Command(BaseCommand):
    def handle(self, *args, **options):
        Park.objects.all().delete()
        response = requests.get(
            "https://developer.nps.gov/api/v1/parks?api_key=GYhnLrZm43nOpAoc5nvpxZa1EyctQywOk6QEnlJ6")
        json = response.json()
        for data in json:
            name = json[data]['fullName']
            location = json[data]['location']
            
            new_park_data = Park.objects.create(
                
                parkName=name['parkName'],
                location=location['location']
                )