from django.db import models


class ParkData(models.Model):
    park_name = models.CharField(max_length=150)
    location = models.CharField(max_length=2)
    url = models.URLField(max_length=200)