from django.shortcuts import render, get_object_or_404 
import json

from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from preferences import models
from preferences import serializers

class PreferenceAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PreferenceSerializer
    def get(self, request):
        try:
            preference = models.Preference.objects.get(client=request.user)
            serializer = self.serializer_class(preference)
            return Response(serializer.data)
        except models.Preference.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        preference, created = models.Preference.objects.get_or_create(client=request.user)
        serializer = self.serializer_class(preference, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
