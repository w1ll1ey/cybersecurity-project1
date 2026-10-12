from django.db import models
from django.conf import settings

class Note(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)