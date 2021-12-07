from django.db import models
from django.contrib.auth.models import User



class Muirist(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # isModerator = models.BooleanField(default=False)
    # isModerater is part of streth portion of build