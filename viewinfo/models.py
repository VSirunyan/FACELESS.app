from django.db import models


class WifiDatabase(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.TimeField()
    type = models.CharField(max_length=100)
    diap = models.FloatField()
    channels = models.IntegerField()
    mac = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    power = models.FloatField()

    def __str__(self):
        return self.mac
