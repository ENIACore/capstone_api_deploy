from django.db import models
from api import globals
from trip import models as trip_models



# Location from json is nested inside result { ... } json obj
class Location(models.Model):

    # One (Trip) to Many (Locations), related name is for reverse lookup from trip
    trip = models.ForeignKey(trip_models.Trip, related_name='locations', on_delete=models.CASCADE)

    addr_address = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    # Update with choices
    business_status = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    formatted_address = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    formatted_phone_number = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    icon = models.URLField(max_length=globals.MAX_CHAR_FIELD)

    icon_background_color = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    icon_mask_base_uri = models.URLField(max_length=globals.MAX_CHAR_FIELD)

    international_phone_number = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    name = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    place_id = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    rating = models.IntegerField()

    reference = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    url = models.URLField(max_length=globals.MAX_CHAR_FIELD)

    user_ratings_total = models.IntegerField()

    vicinity = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    website = models.URLField(max_length=globals.MAX_CHAR_FIELD)

    # Nested obj from json req, geometry: { location: { lat: ..., lng: ...} ....}
    latitude = models.DecimalField(max_digits=globals.MAX_DECIMAL_DIGITS, decimal_places=globals.MAX_DECIMAL_PLACES)

    longitude = models.DecimalField(max_digits=globals.MAX_DECIMAL_DIGITS, decimal_places=globals.MAX_DECIMAL_PLACES)

    # Nested obj from json req, plus_code: { compound_code: ..., global_code: ... }
    compound_code = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    global_code = models.CharField(max_length=globals.MAX_CHAR_FIELD)



    def __unicode__(self):
        return None
