from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'wallet_type', 'card_type', 'currency', 'balance')
    list_filter = ('wallet_type', 'card_type', 'currency')
    search_fields = ('user__phone', 'name')
