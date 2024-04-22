from rest_framework import serializers
from api import globals
from preferences import models

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Preference
        fields = [
            'min_rating', 'max_rating', 'min_price', 'max_price',
            'shopping_mall', 'zoo', 'museum', 'night_club', 'park', 'casino',
            'art_gallery', 'bar', 'campground', 'cafe', 'amusement_park',
            'landmark', 'point_of_interest', 'store', 'restaurant',
            'meal_takeaway', 'tourist_attraction'
        ]

