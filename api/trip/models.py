from django.db import models
from user import models as user_models
from api import globals


class Trip(models.Model):

    # One (Client) to Many (Trips), related name is for reverse lookup from client
    # read this to see options used: https://www.django-rest-framework.org/api-guide/relations/
    client = models.ForeignKey(user_models.Client, related_name='trips', on_delete=models.CASCADE)

    title = models.CharField(max_length=globals.MAX_SHORT_CHAR_FIELD, blank=False, verbose_name="Trip Name")
    description = models.TextField(blank=True, verbose_name="Trip Description")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    favorite = models.BooleanField(default=False, verbose_name="Favorite Trip")

    def __unicode__(self):
        return self.title
