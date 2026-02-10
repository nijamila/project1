from django.db import models
from apps.accounts.models import User
from apps.currency.models import Currency

class Wallet(models.Model):
    WALLET_TYPE = (
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('account', 'Account'),
    )

    CARD_TYPE = (
        ('humo', 'Humo'),
        ('uzcard', 'Uzcard'),
        ('visa', 'Visa'),
        ('mastercard', 'Mastercard'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallet')
    name = models.CharField(max_length=100)
    wallet_type = models.CharField(max_length=10, choices=WALLET_TYPE)
    card_type = models.CharField(max_length=20, choices=CARD_TYPE, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return self.name

