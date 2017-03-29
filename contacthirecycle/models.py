from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class ContactUs(models.Model):

    name = models.ForeignKey('auth.User')
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.name


