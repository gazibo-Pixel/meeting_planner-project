from django.db import models
from django.db.models.fields import CharField
from datetime import time

class Name (models.Model):
    name = models.CharField (max_length=100)
    date = models.DateField()
    Number = models.IntegerField(default=1)
