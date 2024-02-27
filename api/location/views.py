import json

from rest_framework import permissions, viewsets
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

from location import serializers, models

class LocationViewSet(viewsets.ModelViewSet):
    # Must own the trip and be authenticated to create, update, or read it
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.LocationSerializer

    def get_queryset(self): #type: ignore
        return models.Location.objects.filter(trip=self.kwargs['trip_pk'])

    def perform_create(self, serializer):
        serializer.save(trip=self.kwargs['trip_pk'])

        return super(LocationViewSet, self).perform_create(serializer)
