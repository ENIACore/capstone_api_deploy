from rest_framework import serializers
from api import globals
from preferences import models

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = '__all__'
