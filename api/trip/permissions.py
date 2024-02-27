from rest_framework import permissions


class IsTripOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, trip): #type: ignore
        if request.user:
            return trip.client == request.user
        return False
