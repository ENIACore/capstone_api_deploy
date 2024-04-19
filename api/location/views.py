import json

from rest_framework import permissions, viewsets
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

from location import serializers, models
from trip.models import Trip

class LocationViewSet(viewsets.ModelViewSet):
    # Must own the trip and be authenticated to create, update, or read it
    queryset = models.Location.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.LocationSerializer

    def perform_create(self, serializer):
        trip_pk = self.kwargs.get('trip_pk')
        trip_instance = Trip.objects.filter(pk=trip_pk, client=self.request.user).first()
        if trip_instance is None:
            return Response({"error": "Trip not found or you don't have permission to access it"}, status=status.HTTP_404_NOT_FOUND)
        serializer.save(trip=trip_instance )

        return super(LocationViewSet, self).perform_create(serializer)
