"""
seed the db:
python3 manage.py seed_db
(file name)
    """

from django.core.management.base import BaseCommand
import requests
from muiristapi.models import ParkData


class Command(BaseCommand):
    def handle(self, *args, **options):
        ParkData.objects.all().delete()
        response = requests.get(
            "https://developer.nps.gov/api/v1/parks?parkCode=yose&api_key=GYhnLrZm43nOpAoc5nvpxZa1EyctQywOk6QEnlJ6")
        json = response.json()
        for item in json:
            park_name = json[item]['fullName']
            location = json[item]['location']
            
                new_park_data = ParkData.objects.create(
                    
                    parkName=park_name['parkName'],
                    location=location['location'],
                    url= url['url']
                    )