import json

from rest_framework import permissions, viewsets
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

from user.models import Client
from user.permissions import IsUserOwner
from user.serializers import ClientSerializer

from django.contrib.auth import authenticate, login, logout

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from django.shortcuts import get_object_or_404

ensure_csrf = method_decorator(ensure_csrf_cookie)
class CSRFCookie(views.APIView):
    permission_classes = []
    authentication_classes = []
    @ensure_csrf
    def get(self, request):
        return Response("CSRF Cookie set.")

class LoginView(views.APIView):

    permission_classes = [permissions.AllowAny]

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
                response = Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_403_FORBIDDEN)
                return response
        else:
            response = Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_403_FORBIDDEN)
            return response

class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)

# Used to get only currently logged in user, ClientViewSet is for all users logged in user has permission to
class ClientView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        if (self.request.user.is_authenticated):
            client = get_object_or_404(Client, username=request.user.username)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        else:
            response = Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
            # Set WWW-Authenticate header to prevent default browser pop-up, this is because this endpoint is only for form based authentication
            response['WWW-Authenticate'] = 'FormBased'
            return response

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
            user = Client.objects.create_user(**serializer.validated_data) #type: ignore

            login(request, user)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
