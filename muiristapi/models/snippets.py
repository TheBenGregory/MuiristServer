from django.db import models



class Snippet(models.Model):

    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)
    muirist = models.ForeignKey("Muirist", on_delete=models.CASCADE)
    park = models.ForeignKey("Park", on_delete=models.CASCADE)