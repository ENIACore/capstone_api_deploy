from rest_framework import serializers
from api import globals
from location import models

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Location
        fields = ['id', 'google_location_id', ]
        read_only_fields = ['id']
