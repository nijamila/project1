from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SupportMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_messages')
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
