from django.db import models
from django.utils import timezone

class Advert(models.Model):

    # author is linked to a registered
    # user in the 'auth_user' table.
    advertiser = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    description = models.TextField()
    condition = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    daily_rental_rate = models.IntegerField(default=0)
    daily_insurance_cover_rate = models.IntegerField(default=0)
    pickup_location = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.item
