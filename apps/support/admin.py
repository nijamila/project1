from django.contrib import admin
from .models import SupportMessage

@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'replied_at', 'message', 'reply')
    readonly_fields = ('user', 'created_at', 'replied_at')
    search_fields = ('user__phone', 'message', 'reply')
    list_filter = ('created_at',)
