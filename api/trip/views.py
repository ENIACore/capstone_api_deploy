import json

from rest_framework import permissions, viewsets
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

import models
import serializers

from trip import permissions as trip_permissions

class TripViewSet(viewsets.ModelViewSet):
    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer
    permission_classes = [permissions.IsAuthenticated, trip_permissions.IsTripOwner]
