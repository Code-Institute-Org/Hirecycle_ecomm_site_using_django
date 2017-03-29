from django.conf.urls import url
from .views import contactus

urlpatterns = [
    url(r'^$', contactus, name='ContactUs'),
]