from django.shortcuts import render, get_object_or_404, redirect
from .models import Advert, InsurancePackage
from django.utils import timezone
from .forms import AdvertPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def advertlist(request):
        adverts = Advert.objects.filter(available_from__lte=timezone.now()
                                    ).order_by('-available_from')
        return render(request, "advertlist.html", {'adverts': adverts})


def addetails(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    advert = get_object_or_404(Advert, pk=id)
    insurance_package = get_object_or_404(InsurancePackage, pk=id)
    advert.views += 1
    advert.save()
    return render(request, "addetails.html", {'advert': advert,'insurance_package': insurance_package})

@login_required(login_url="/user/login?next=ads/new")
def new_ad(request):
    if request.method == "POST":
        form = AdvertPostForm(request.POST, request.FILES)
        if form.is_valid():
            advert = form.save(commit=False)
            advert.advertiser = request.user
            advert.save()
            return redirect(addetails, advert.pk)
    else:
        form = AdvertPostForm()
    return render(request, 'adform.html', {'form': form})

@login_required(login_url="/user/login?next=ads/edit/")
def edit_ad(request, id):
   advert = get_object_or_404(Advert, pk=id)
   if request.method == "POST":
       form = AdvertPostForm(request.POST, request.FILES, instance=advert)
       if form.is_valid():
           advert = form.save(commit=False)
           advert.advertiser = request.user
           advert.save()
           return redirect(addetails, advert.pk)
   else:
       form = AdvertPostForm(instance=advert)
   return render(request, 'adform.html', {'form': form})