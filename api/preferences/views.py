from django.shortcuts import render
import json
from rest_framework import serializers
from rest_framework import permissions, viewsets
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

from preferences import models, serializers

class PreferenceViewSet(viewsets.ModelViewSet):
    # Must be authenticated to create, update, or read preferences
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Preference.objects.all()
    serializer_class = serializers.PreferenceSerializer

    def get_queryset(self):
        trip_pk = self.kwargs.get('trip_pk')
        if trip_pk is not None:
            return self.queryset.filter(trip=trip_pk)
        else:
            # Handle the case where trip_pk is missing
            return self.queryset.none()

    def perform_create(self, serializer):
        trip_pk = self.kwargs.get('trip_pk')
        if trip_pk is not None:
            serializer.save(trip=trip_pk)
        else:
            # Handle the case where trip_pk is missing
            # For example, raise an exception or return an appropriate response
            pass

# Create your views here.
