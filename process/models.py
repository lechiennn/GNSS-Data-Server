from django.db import models
from django.utils.text import slugify

from processServer.models import BaseModel

__all__ = (
    'Station',
    'Data',
)


class Station(BaseModel):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, null=True, blank=True)
    location = models.TextField(blank=True)

    def save(self, *args, **kwagrs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Station, self).save(*args, **kwagrs)

    def __str__(self):
        return self.slug


class Data(BaseModel):
    station = models.ForeignKey(
        Station, blank=True, null=True, on_delete=models.CASCADE)
    temperature = models.FloatField(blank=True)
    precipitation = models.FloatField(blank=True)
    created_at = models.DateTimeField()
