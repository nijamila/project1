from django.contrib import admin
from .models import Income, Expense, Transfer

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet', 'category', 'amount', 'date')
    list_filter = ('wallet', 'category', 'date')
    search_fields = ('user__phone', 'category__name')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet', 'category', 'amount', 'date')
    list_filter = ('wallet', 'category', 'date')
    search_fields = ('user__phone', 'category__name')

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('user', 'from_wallet', 'to_wallet', 'amount', 'date')
    list_filter = ('from_wallet', 'to_wallet', 'date')
    search_fields = ('user__phone',)
