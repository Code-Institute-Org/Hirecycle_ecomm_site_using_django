from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import CartItem
from django.contrib.auth.decorators import login_required
from adverts.models import Advert
from payments.forms import MakePaymentForm
from django.template.context_processors import csrf
from django.contrib import messages
from django.conf import settings
import stripe

# stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url="/login")
def user_cart(request):
    cartItems = CartItem.objects.filter(user=request.user)
    total = 0
    for item in cartItems:
        total += item.no_of_days * (item.advert.daily_rental_rate)
        # total += item.no_of_days * (item.product.daily_rental_rate + item.insurancepackage.insurance_package_rate)

    if request.method == 'POST':
        form = MakePaymentForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined. Please try again")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                CartItem.objects.filter(user=request.user).delete()
                return redirect(reverse('advertlist'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        if len(cartItems) == 0:
            return render(request, 'empty_cart.html')

        form = MakePaymentForm()

    args = {'form': form,
            'items': cartItems,
            'total': total,
            'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'cart.html', args)




@login_required(login_url="/login")
def add_to_cart(request, id):
    advert = get_object_or_404(Advert, pk=id)
    # no_of_days=int(request.POST.get('no_of_days'))
    no_of_days = 1

    try:
        cartItem = CartItem.objects.get(user=request.user, advert=advert)
        cartItem.no_of_days += no_of_days
    except CartItem.DoesNotExist:
        cartItem = CartItem(
            user=request.user,
            advert=advert,
            no_of_days=no_of_days
        )

    cartItem.save()
    return redirect(reverse('cart'))


def remove_from_cart(request, id):
    CartItem.objects.get(id=id).delete()
    return redirect(reverse('cart'))

