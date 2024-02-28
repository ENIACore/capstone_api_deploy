import json

from rest_framework import permissions, viewsets
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

from trip import models, serializers

from trip import permissions as trip_permissions

class TripViewSet(viewsets.ModelViewSet):
    # Must own the trip and be authenticated to create, update, or read it
    permission_classes = [permissions.IsAuthenticated, trip_permissions.IsTripOwner]
    serializer_class = serializers.TripSerializer

    # Ensures that when a user queries a specifc trip or all trips using /trips or /trips/<pk> it will only query for trips owned by that user
    def get_queryset(self): #type: ignore
        return models.Trip.objects.filter(client=self.request.user)

    # Adds author data to serializer to associate created trip with user
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

        return super(TripViewSet, self).perform_create(serializer)
