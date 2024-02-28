import json

from rest_framework import permissions, viewsets
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

from user.models import Client
from user.permissions import IsUserOwner
from user.serializers import ClientSerializer

from django.contrib.auth import authenticate, login, logout

class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        client = authenticate(email=email, password=password)

        if client is not None:
            if client.is_active:
                login(request, client)

                serialized = ClientSerializer(client)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)

class ClientViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self): #type: ignore
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        elif self.request.method == 'POST':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated(), IsUserOwner()]

    def create(self, request): #type: ignore
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Client.objects.create_user(**serializer.validated_data) #type: ignore

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)
