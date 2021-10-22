from django.db import models
from django.conf import settings
# Create your models here.


class ControlStation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=8)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=8)
    x_northing = models.DecimalField(
        max_digits=22, decimal_places=4)
    y_easting = models.DecimalField(
        max_digits=22, decimal_places=4)
    # height = models.DecimalField(max_digits=22,decimal_places=4,blank=True,null=True)
    height = models.CharField(max_length=100, default='N/A')
    description = models.TextField(blank=True, null=True)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='control',
                               on_delete=models.CASCADE
                               )

    def __str__(self):
        return self.name
