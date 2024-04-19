from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Preference

class PreferenceAPITests(APITestCase):
    def setUp(self):
        # Create some sample preferences
        Preference.objects.create(
            min_rating=3.0,
            max_rating=5.0,
            min_price=1,
            max_price=3,
            shopping_mall=True,
            zoo=False,
            museum=True,
            night_club=False,
            park=True,
            casino=False,
            art_gallery=True,
            bar=False,
            campground=True,
            cafe=False,
            amusement_park=True,
            landmark=False,
            point_of_interest=True,
            store=False,
            restaurant=True,
            meal_takeaway=False,
            tourist_attraction=True
            # Add more fields based on your model structure
        )

    def test_get_preferences(self):
        url = reverse('preferences-list')  # Adjust the URL name if necessary
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions to check the response data

    def test_create_preference(self):
        url = reverse('preferences-list')  # Adjust the URL name if necessary
        data = {
            'min_rating': 2.0,
            'max_rating': 4.0,
            'min_price': 0,
            'max_price': 2,
            'shopping_mall': True,
            'zoo': True,
            'museum': False,
            'night_club': False,
            'park': True,
            'casino': False,
            'art_gallery': True,
            'bar': False,
            'campground': True,
            'cafe': False,
            'amusement_park': True,
            'landmark': False,
            'point_of_interest': True,
            'store': False,
            'restaurant': True,
            'meal_takeaway': False,
            'tourist_attraction': True
            # Add more fields based on your serializer structure
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add more assertions to check the created object

    # Add more test cases as needed

