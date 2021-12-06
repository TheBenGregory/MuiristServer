from django.db import models
from django.contrib.auth.models import User



class Muirist(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # isModerator = models.BooleanField(default=False)
    # isModerater is part of streth portion of build