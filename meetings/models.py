from datetime import time
from django.db import models
from django.db.models.fields import CharField

class Room(models.Model):
    room = models.CharField(max_length=25)
    Number = models.IntegerField()
    Floor = models.IntegerField()

class Meeting(models.Model):
    title = models.CharField (max_length=100)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)



