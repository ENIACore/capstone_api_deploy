from rest_framework.test import APITestCase
from rest_framework import status
from location.models import Location
from trip.models import Trip
from user.models import Client
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, force_authenticate

class LocationTests(APITestCase):

    def setUp(self):
        self.user = Client.objects.create_user(email='test@example.com', password='testpassword', username='testuser')
        self.trip_instance =  Trip.objects.create(name="Test Trip", client_id=1)
        
        self.location_data = {
            'trip': self.trip_instance,
            'addr_address': "https://api.chases-server.com/api/v1/users",
            'business_status': "test",
            'formatted_address': "123 Anywhere USA",
            'formatted_phone_number': "123-456-7890",
            'icon': "https://api.chases-server.com/api/v1/users",
            'icon_background_color': "BLUE",
            'icon_mask_base_uri': "https://api.chases-server.com/api/v1/users",
            'international_phone_number': "020-1234-1234",
            'name': "Steve",
            'place_id': "placeID",
            'rating': 5,
            'reference': "test",
            'url': "https://api.chases-server.com/api/v1/users",
            'user_ratings_total': 13,
            'vicinity': "test",
            'website': "https://api.chases-server.com/api/v1/users",
            'latitude': 100.5,
            'longitude': 73.4,
            'compound_code': "test code",
            'global_code': "test global",
        }

    def test_create_location(self):
        location = Location.objects.create(**self.location_data)
        created_location = Location.objects.get(pk=location.id)

        self.assertEqual(created_location.addr_address, self.location_data['addr_address'])
        self.assertEqual(created_location.business_status, self.location_data['business_status'])
        self.assertEqual(created_location.trip, self.trip_instance)

    def test_read_location(self):
        location = Location.objects.create(**self.location_data)
        url = reverse('locations-detail', kwargs={'trip_pk': self.trip_instance.id, 'pk': location.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['addr_address'], self.location_data['addr_address'])
        
    def test_delete_location(self):
        location = Location.objects.create(**self.location_data)
        url = reverse('locations-detail', kwargs={'trip_pk': location.trip.id, 'pk': location.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Location.DoesNotExist):
            Location.objects.get(pk=location.id)



