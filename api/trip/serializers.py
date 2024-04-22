from rest_framework import serializers
from trip import models

class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Trip

        fields = ['id', 'title', 'description', 'favorite', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
