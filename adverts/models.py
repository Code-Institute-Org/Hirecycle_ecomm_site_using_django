from django.db import models
from django.utils import timezone

class Advert(models.Model):

    # author is linked to a registered
    # user in the 'auth_user' table.
    advertiser = models.ForeignKey('auth.User')
    category = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    description = models.TextField()
    condition = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    pickup_location = models.CharField(max_length=200)
    original_retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_rental_rate = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def advertised_rental_rate(self):
        return (self.daily_rental_rate)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.item
