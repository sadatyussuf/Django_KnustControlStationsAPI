from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import ControlStation


class ControlStationSerializer(serializers.ModelSerializer):
    poster_id = serializers.ReadOnlyField(source='poster.id')
    poster = serializers.ReadOnlyField(source='poster.username')

    class Meta:
        model = ControlStation
        fields = ['id', 'name', 'latitude', 'longitude',
                  'x_northing', 'y_easting', 'height', 'description', 'poster', 'poster_id']
