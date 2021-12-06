from django.db import models



class FavoritePark(models.Model):

    parks = models.ForeignKey("Park", on_delete=models.CASCADE)
    muirist = models.ForeignKey("Muirist", on_delete=models.CASCADE)
    