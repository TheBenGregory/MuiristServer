from django.db import models



class Park(models.Model):

    name = models.CharField(max_length=70)
    location = models.CharField(max_length=35)