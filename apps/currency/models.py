from django.db import models
from apps.accounts.models import User
from decimal import Decimal

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # UZS, USD, EUR
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.code} - {self.name}"

    def get_rate_to(self, user, target_currency):
        if self == target_currency:
            return Decimal('1')
        try:
            rate_obj = UserCurrencyRate.objects.get(
                user=user,
                from_currency=self,
                to_currency=target_currency
            )
            return Decimal(rate_obj.rate)
        except UserCurrencyRate.DoesNotExist:
            return Decimal('1')


class UserCurrencyRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name='from_rates'
    )
    to_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name='to_rates'
    )
    rate = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        unique_together = ('user', 'from_currency', 'to_currency')