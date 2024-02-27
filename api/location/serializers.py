from rest_framework import serializers
from api import globals
from location import models

class GeometryLocationSerializer(serializers.Serializer):
    lng = serializers.DecimalField(max_digits=globals.MAX_DECIMAL_DIGITS, decimal_places=globals.MAX_DECIMAL_PLACES, source='latitude')

    lat = serializers.DecimalField(max_digits=globals.MAX_DECIMAL_DIGITS, decimal_places=globals.MAX_DECIMAL_PLACES, source='longitude')

class GeometrySerializer(serializers.Serializer):
    location = GeometryLocationSerializer(source='*')


class PlusCodeSerializer(serializers.Serializer):
    # Nested obj from json req, plus_code: { compound_code: ..., global_code: ... }
    compound_code = serializers.CharField(max_length=globals.MAX_CHAR_FIELD)

    global_code = serializers.CharField(max_length=globals.MAX_CHAR_FIELD)

class LocationSerializer(serializers.ModelSerializer):
    # Nested obj from json req, geometry: { location: { lat: ..., lng: ...} ....}
    geometry = GeometrySerializer(source='*')
    plus_code = PlusCodeSerializer(source='*')

    class Meta:
        model = models.Location
        fields = ['id', 'addr_address', 'business_status', 'formatted_address', 'formatted_phone_number', 'icon', 'icon_background_color', 'icon_mask_base_uri',
                        'international_phone_number', 'name', 'place_id', 'rating', 'reference', 'url', 'user_ratings_total', 'vicinity', 'website', 'geometry',
                        'plus_code']
        read_only_fields = ['id']
