from django import forms
from .models import Advert


class AdvertPostForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = (
            'advertiser',
            'category',
            'item',
            'description',
            'condition',
            'image',
            'original_retail_price',
            'daily_rental_rate',
            'insurance_package',
            'pickup_location')
