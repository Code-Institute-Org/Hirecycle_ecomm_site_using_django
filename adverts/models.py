from django.db import models
from django.utils import timezone

class Advert(models.Model):

    # author is linked to a registered
    # user in the 'auth_user' table.
    advertiser = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    daily_rental_rate = models.IntegerField(default=0)
    pickup_location = models.TextField()
    condition = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title
