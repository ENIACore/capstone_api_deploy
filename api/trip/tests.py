from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from trip.models import Trip
from user.models import Client

class TripTests(APITestCase):

    def setUp(self):
        self.user = Client.objects.create_user(email='test@example.com', password='testpassword', username='testuser')
        
        self.trip_instance = Trip.objects.create(client=self.user, name='Test Trip', description='Test description', favorite=False)

        self.trip_data = {
            'client': self.user.id,
            'name': 'Test Trip',
            'description': 'This is a test trip.',
            'favorite': True,
        }

    def test_create_trip(self):
        url = reverse('trips-list')  
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, self.trip_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_trip(self):
        url = reverse('trips-detail', kwargs={'pk': self.trip_instance.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Trip')
        self.assertEqual(response.data['description'], 'Test description')

    def test_update_trip(self):
        url = reverse('trips-detail', kwargs={'pk': self.trip_instance.id})
        self.client.force_authenticate(user=self.user)

        updated_data = {
            'name': 'Updated Trip',
            'description': 'Updated description',
            'favorite': True,
        }

        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_trip = Trip.objects.get(pk=self.trip_instance.id)
        self.assertEqual(updated_trip.name, 'Updated Trip')
        self.assertEqual(updated_trip.description, 'Updated description')
        self.assertEqual(updated_trip.favorite, True)

    def test_delete_trip(self):
        url = reverse('trips-detail', kwargs={'pk': self.trip_instance.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Trip.DoesNotExist):
            Trip.objects.get(pk=self.trip_instance.id)
