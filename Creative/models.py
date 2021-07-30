from django.db import models
from django.db.models.fields import CharField

class NAME (models.Model):
    name = models.CharField (max_length=100)
    date = models.DateField()
