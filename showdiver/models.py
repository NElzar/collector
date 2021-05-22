from django.db import models


class Event(models.Model):
    uuid = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    description = models.TextField()
    start = models.DateTimeField()
    poster = models.URLField()


class Ticket(models.Model):
    sector = models.CharField(max_length=256)
    site = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')