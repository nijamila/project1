from django.contrib import admin
from .models import SupportMessage

@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_admin', 'is_read', 'created_at')
    list_filter = ('is_admin', 'is_read', 'created_at')
    search_fields = ('user__phone', 'message')
