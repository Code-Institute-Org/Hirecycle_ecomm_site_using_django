from __future__ import unicode_literals

from django.db import models
from adverts.models import Advert
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User)
    advert = models.ForeignKey(Advert)
    pick_up_date = models.DateField(blank=True, null=True)
    no_of_days = models.IntegerField(default=1)

    def __str__(self):
        return "{0} ({1})".format(self.advert.name, self.no_of_days)