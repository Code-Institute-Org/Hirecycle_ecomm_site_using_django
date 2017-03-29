from django.db import models
from django.utils import timezone

class Advert(models.Model):

    # author is linked to a registered
    # user in the 'auth_user' table.
    advertiser = models.ForeignKey('auth.User')
    category = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    description = models.TextField()
    condition = models.CharField(max_length=200)
    available_from = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    pickup_location = models.CharField(max_length=200)
    original_retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_rental_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.item

class InsurancePackage(models.Model):

    NoInsurance = "I don't need insurance"
    Bronze = "Bronze"
    Silver = "Silver"
    Gold = "Gold"

    insurance_package_choices=(
        (NoInsurance, "I don't need insurance"),
        (Bronze, "Bronze"),
        (Silver, "Silver"),
        (Gold, "Gold")
    )

    insurance_package = models.CharField(max_length=100, choices=insurance_package_choices, default=NoInsurance)
    insurance_package_rate = models.DecimalField(max_digits=4, decimal_places=2, default=1)
    def publish(self):
        self.save()

    def __unicode__(self):
        return self.insurance_package

        # @property
        # def advertised_daily_rental_rate(self):
        #     daily_rental_rate = self.daily_rental_rate
        #     insurance_package = self.insurance_package
        #     return (daily_rental_rate * insurance_package)
    # daily_insurance_cover_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # # insurance_package_choices = (
    # #     (1.0,"I don't need insurance"),
    # #     (1.2,"Bronze"),
    # #     (1.4,"Silver"),
    # #     (1.5,"Gold"),
    # # )
    # insurance_package = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2,
    #     choices=(
    #     (1.0, "I don't need insurance"),
    #     (1.2, "Bronze"),
    #     (1.4, "Silver"),
    #     (1.5, "Gold"))
    # )
