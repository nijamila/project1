from django import forms
from .models import Currency, UserCurrencyRate

class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ['code', 'name']

class UserCurrencyRateForm(forms.ModelForm):
    class Meta:
        model = UserCurrencyRate
        fields = ['from_currency', 'to_currency', 'rate']
