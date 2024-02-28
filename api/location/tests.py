from django.test import TestCase
from api import models 

class LocationTests(TestCase):

    def test_tag_model_str(self)
        task = models.Task.objects.create
        (
            addr_address = "https://api.chases-server.com/api/v1/users",
            business_status = "test",
            formatted_address = "123 Anywhere USA",
            formatted_phone_number = "123-456-7890",
            icon = "https://api.chases-server.com/api/v1/users",
            icon_background_color = "BLUE"
            icon_mask_base_uri = "https://api.chases-server.com/api/v1/users",
            international_phone_number = "020-1234-1234",
            name = "Steve",
            place_id = "placeID",
            rating = "5",
            reference = "test",
            url = "https://api.chases-server.com/api/v1/users",
            user_ratings_total = "13",
            vicinity = "test",
            website = "https://api.chases-server.com/api/v1/users",
            geometry_location_lat = "100.5",
            geometry_location_lng = "73.4",
            geometry_viewport_northeast_lat = "21.6",
            geometry_viewport_northeast_lng = "158.9",
            geometry_viewport_northeast_lng = "210.4",
            geometry_viewport_northeast_lng = "11.9",
            plus_code_compound_code = "test code",
            plus_code_global_code = "test global",
        )

        self.assertEqual(unicode(task), task.None)
# Create your tests here.
