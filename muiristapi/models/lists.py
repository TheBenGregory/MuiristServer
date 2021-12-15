from django.db import models



class List(models.Model):


    muirist = models.ForeignKey("Muirist", on_delete=models.CASCADE)
    park = models.ForeignKey("Park", on_delete=models.CASCADE)
    