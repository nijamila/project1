from django import forms
from .models import Wallet

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['name', 'wallet_type', 'card_type', 'currency', 'balance']
