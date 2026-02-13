from django.contrib import admin
from django.utils.html import format_html
from .models import SupportMessage

@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_phone', 'short_message', 'created_at', 'replied_at', 'reply_status', 'reply_preview','reply')
    list_editable = ('reply',)
    readonly_fields = ('user', 'created_at', 'replied_at')
    search_fields = ('user__phone', 'message', 'reply')
    list_filter = ('created_at', 'replied_at')
    ordering = ('-created_at',)


    def user_phone(self, obj):
        return obj.user.phone
    user_phone.short_description = 'User'


    def short_message(self, obj):
        return (obj.message[:50] + '...') if len(obj.message) > 50 else obj.message
    short_message.short_description = 'Message'


    def reply_status(self, obj):
        if obj.reply:
            return format_html('<span style="color:green;font-weight:bold;">Yes</span>')
        return format_html('<span style="color:red;font-weight:bold;">No</span>')
    reply_status.short_description = 'Replied?'
    reply_status.admin_order_field = 'reply'

    def reply_preview(self, obj):
        if obj.reply:
            return (obj.reply[:50] + '...') if len(obj.reply) > 50 else obj.reply
        return "-"
    reply_preview.short_description = 'Reply Preview'
