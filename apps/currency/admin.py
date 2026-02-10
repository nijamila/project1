from django.contrib import admin
from .models import Currency, UserCurrencyRate

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')

@admin.register(UserCurrencyRate)
class UserCurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('user', 'from_currency', 'to_currency', 'rate')
    list_filter = ('from_currency', 'to_currency')
    search_fields = ('user__phone', 'user__first_name', 'user__last_name')
