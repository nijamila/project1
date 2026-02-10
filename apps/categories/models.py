from django.db import models
from apps.accounts.models import User

class Category(models.Model):
    CATEGORY_TYPE = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Null means global default category"
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CATEGORY_TYPE)
    is_default = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'name', 'type')
        ordering = ['type', 'name']

    def __str__(self):
        return f"{self.name} ({self.type})"
