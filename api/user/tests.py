from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Client

class ClientTests(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.user = Client.objects.create_user(**self.user_data)

    def authenticate_user(self):
        # Authenticate the user and obtain a token
        response = self.client.post('/login/', {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_create_user(self):
        # Authenticate the user
        token = self.authenticate_user()

        # Use the token in subsequent requests
        headers = {'Authorization': f'Bearer {token}'}
        
        # Create a new user
        data = {
            'email': 'newuser@example.com',
            'username': 'newuser',
            'password': 'newpassword',
        }
        response = self.client.post('/users/', data, headers=headers)
        
        # Check if the user is created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 2)  # Check if user is created in the database

        # Optionally, you can add more assertions to check the response content or other details.
        self.assertEqual(response.data['email'], 'newuser@example.com')
        self.assertEqual(response.data['username'], 'newuser')
