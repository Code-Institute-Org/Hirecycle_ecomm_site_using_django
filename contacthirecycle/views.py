from django.shortcuts import render, redirect
from.forms import ContactUsForm

# Create your views here.
def contactus(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST, request.FILES)
        if form.is_valid():
            ContactUs = form.save(commit=False)
            ContactUs.name = request.user
            ContactUs.save()
            return redirect(ContactUs, contacthirecycle.pk)

    else:
        form = ContactUsForm()
    return render(request, "contactus.html", {'form': form})
