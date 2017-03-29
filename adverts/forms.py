from django import forms
from .models import Advert


class AdvertPostForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ('advertiser', 'category', 'item', 'description', 'condition', 'created_date', 'published_date', 'image', 'daily_rental_rate', 'daily_insurance_cover_rate', 'pickup_location')
