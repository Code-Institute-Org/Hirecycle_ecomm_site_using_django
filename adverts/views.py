from django.shortcuts import render
from .models import Advert
from django.utils import timezone

# Create your views here.

def advertlist(request):
        adverts = Advert.objects.filter(published_date__lte=timezone.now()
                                    ).order_by('-published_date')
        return render(request, "advertlist.html", {'adverts': adverts})


def advertdetails(request):
    adverts = Advert.objects.filter(published_date__lte=timezone.now()
                                    ).order_by('-published_date')
    return render(request, "advertdetails.html", {'adverts': adverts})