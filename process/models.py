from django.db import models

# Create your models here.
__all__ = (
    'Station',
    'Data',
)


class Station(models.Model):
    name = models.CharField(max_length=30)

class Data(models.Model):
    station = models.ForeignKey(Station, blank=True, null=True, on_delete=models.SET_NULL)
    temperature = models.FloatField(blank=True)
    precipitation = models.FloatField(blank=True)
    created_at = models.DateTimeField()
