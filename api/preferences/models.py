from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from user import models as user_models

class Preference(models.Model):

    client = models.OneToOneField(user_models.Client, related_name='preference', on_delete=models.CASCADE)
    
    min_rating = models.FloatField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    max_rating = models.FloatField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    min_price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    max_price = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    #Google types
    shopping_mall = models.BooleanField(default=False)
    zoo = models.BooleanField(default=False)
    museum = models.BooleanField(default=False)
    night_club = models.BooleanField(default=False)
    park = models.BooleanField(default=False)
    casino = models.BooleanField(default=False)
    art_gallery = models.BooleanField(default=False)
    bar = models.BooleanField(default=False)
    campground = models.BooleanField(default=False)
    cafe = models.BooleanField(default=False)
    amusement_park = models.BooleanField(default=False)
    landmark = models.BooleanField(default=False)
    
    point_of_interest = models.BooleanField(default=False)
    store = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    meal_takeaway = models.BooleanField(default=False)
    tourist_attraction = models.BooleanField(default=False)
        

    def __unicode__(self):
        return None
