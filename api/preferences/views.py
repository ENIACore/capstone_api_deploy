from django.shortcuts import render
import json

from rest_framework import permissions, viewsets
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

from preferences import models

class PreferenceViewSet(viewsets.ModelViewSet):
    # Must be authenticated to create, update, or read preferences
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Preference.objects.all()
    serializer_class = serializers.PreferenceSerializer

    def get_queryset(self):
        return self.queryset.filter(trip=self.kwargs['trip_pk'])

    def perform_create(self, serializer):
        serializer.save(trip=self.kwargs['trip_pk'])

# Create your views here.
