from django.db import models
from apps.accounts.models import User
from apps.wallets.models import Wallet
from apps.categories.models import Category
from django.core.exceptions import ValidationError

class BaseTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='transactions/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='outgoing')
    to_wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='incoming')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()

    def clean(self):
        if self.from_wallet == self.to_wallet:
            raise ValidationError("Cannot transfer to the same wallet")

class Income(BaseTransaction):
    def clean(self):
        if self.category.type != 'income':
            raise ValidationError('Income must use an income category')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Expense(BaseTransaction):
    def clean(self):
        if self.category.type != 'expense':
            raise ValidationError('Expense must use an expense category')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
