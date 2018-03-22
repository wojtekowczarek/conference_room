from django.db import models
from datetime import datetime


TAKEN = (
    (True, 'Yes'),
    (False, 'No')
)


class Room(models.Model):
    name = models.CharField(max_length=32)
    number = models.IntegerField()
    description = models.CharField(max_length=128)


class Reservation(models.Model):
    date = models.DateTimeField()
    taken = models.BooleanField(choices=TAKEN)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
