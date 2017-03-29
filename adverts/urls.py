from django.conf.urls import url
from .views import advertlist, addetails, new_ad, edit_ad

urlpatterns = [
    url(r'^$', advertlist, name='advertlist'),
    url(r'^(?P<id>\d+)/$', addetails, name='addetails'),
    url(r'^new/$', new_ad, name='new_ad'),
    url(r'^(?P<id>\d+)/edit$', edit_ad, name='edit_ad'),
]