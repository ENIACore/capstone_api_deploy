from django.db import models
from api import globals
from trip import models as trip_models



# Location from json is nested inside result { ... } json obj
class Location(models.Model):

    # One (Trip) to Many (Locations), related name is for reverse lookup from trip
    trip = models.ForeignKey(trip_models.Trip, related_name='locations', on_delete=models.CASCADE)

    google_location_id = models.TextField(blank=True, verbose_name="Google location ID")

    def __unicode__(self):
        return self.google_location_id
