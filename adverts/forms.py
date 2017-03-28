from django import forms
from .models import Advert


class AdvertPostForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ('title', 'content', 'image')