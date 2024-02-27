from django.db import models
from api import globals


# Location from json is nested inside result { ... } json obj
class Location(models.Model):

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
    geometry_location_lat = models.DecimalField()

    geometry_location_lng = models.DecimalField()

    # Nested x2 obj from json req, geometry: { location: ...., viewport: { northeast: { lat: ..., lng: ... }, southwest: { lat ..., lng: ...} } }
    geometry_viewport_northeast_lat = models.DecimalField()

    geometry_viewport_northeast_lng = models.DecimalField()

    geometry_viewport_southwest_lat = models.DecimalField()

    geometry_viewport_southwest_lng = models.DecimalField()

    # Nested obj from json req, plus_code: { compound_code: ..., global_code: ... }
    plus_code_compound_code = models.CharField(max_length=globals.MAX_CHAR_FIELD)

    plus_code_global_code = models.CharField(max_length=globals.MAX_CHAR_FIELD)



    def __unicode__(self):
        return None
