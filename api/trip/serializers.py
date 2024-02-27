from rest_framework import serializers
from user import serializers as user_serializers
import models
from location import models as location_models


class TripSerializer(serializers.ModelSerializer):
    # Include client information when sending Trip info, not required for deserialization
    client = user_serializers.ClientSerializer(read_only=True, required=False)
    # Include all locations when sending Trip info, not required for deserialization
    locations = serializers.PrimaryKeyRelatedField(location_models.Location, required=False, many=True)

    class Meta:
        model = models.Trip

        fields = ('id', 'client', 'name', 'description', 'favorite', 'locations', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
