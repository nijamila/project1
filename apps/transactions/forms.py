from django import forms
from .models import Income, Expense, Transfer
from apps.wallets.models import Wallet
from apps.categories.models import Category


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['from_wallet', 'to_wallet', 'amount', 'date']


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = [
            'wallet',
            'category',
            'amount',
            'date',
            'description',
            'photo',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.fields['wallet'].queryset = Wallet.objects.filter(user=user)
        self.fields['category'].queryset = Category.objects.filter(
            user=user,
            type='income'
        )

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            'wallet',
            'category',
            'amount',
            'date',
            'description',
            'photo',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['wallet'].queryset = Wallet.objects.filter(user=user)
        self.fields['category'].queryset = Category.objects.filter(
            user=user,
            type='expense'
        )
