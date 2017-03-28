from django.conf.urls import url
from .views import advertlist, advertdetails

urlpatterns = [
    url(r'^$', advertlist, name='advertlist'),
    url(r'^addetails/', advertdetails, name='advertdetails'),
]